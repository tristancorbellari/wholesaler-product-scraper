import re
import requests
import util.constants as c

from models.product import Product


def regex_match(regex, text):
    result = re.search(regex, text)

    if result:
        return result.group(1)

    return ""


def product_from_text(text, url):
    site_category = url[(url.rfind("/") + 1) :]
    image_url = regex_match(r"href: \'(.*?)\'", text)
    code = regex_match(r'<span class=\\"medgreen\\">(.*?)<br \/>', text)
    title = regex_match(r"<strong>(.*?)<\/strong>", text)
    price = regex_match(r"Price: R (.*?)<br \/>", text)
    description = regex_match(
        r'<span class=\\"popup-full-description\\"><p>(.*?)<\/p><\/span>', text
    )

    return Product(site_category, image_url, code, title, price, description)


def scrape_webpage(url):
    print("Starting website scraping...")

    page = requests.get(url)
    data = page.text

    result = re.search(
        r"var gallery = \[\{name: \'products\',files: \[\{(.*?)\}\]", data
    )

    print("Website scraping completed!\n")

    if result:
        return [product_from_text(p, url) for p in result.group(1).split(r"},{ ")]

    return None
