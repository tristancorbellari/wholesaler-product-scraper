import re
import requests
import util.constants as c


def regex_match(regex, text):
    result = re.search(regex, text)

    if result:
        return result.group(1)

    return ""


def product_from_text(text, url):
    image_url = regex_match(r"href: \'(.*?)\'", text)
    code = regex_match(r'<span class=\\"medgreen\\">(.*?)<br \/>', text)
    title = regex_match(r"<strong>(.*?)<\/strong>", text)
    price = regex_match(r"Price: R (.*?)<br \/>", text)
    description = regex_match(
        r'<span class=\\"popup-full-description\\"><p>(.*?)<\/p><\/span>', text
    )

    product = {
        "Site Category": url[(url.rfind('/') + 1):],
        "Image Src": image_url,
        "Code": code,
        "Title": title,
        "Price": price,
        "Body (HTML)": description,
        "Collection": "",
        "Vendor": c.VENDOR,
        "Weight": "",
        "Weight Unit": c.DEFAULT_WEIGHT_UNIT,
        "Status": c.DEFAULT_STATUS
    }

    return product


def scrape_webpage(url):
    page = requests.get(url)
    data = page.text

    result = re.search(
        r"var gallery = \[\{name: \'products\',files: \[\{(.*?)\}\]", data
    )
    if result:
        return [product_from_text(p, url) for p in result.group(1).split(r"},{ ")]

    return None
