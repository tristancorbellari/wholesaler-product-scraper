import re
import requests
import util.constants as c
import util.operations as o

from models.product import Product


def regex_match(regex, text):
    result = re.search(regex, text)

    if result:
        return result.group(1)

    return ""


def product_from_text(text, url):
    site_category = o.end_of_url(url)
    image_url = regex_match(r"href: \'(.*?)\'", text)
    code = regex_match(r'<span class=\\"medgreen\\">(.*?)<br \/>', text)
    title = regex_match(r"<strong>(.*?)<\/strong>", text)
    price = regex_match(r"Price: R (.*?)<br \/>", text)
    description = regex_match(
        r'<span class=\\"popup-full-description\\"><p>(.*?)<\/p><\/span>', text
    )

    return Product(site_category, image_url, code, title, price, description)


def scrape_webpage(url):
    print("Scraping {}...".format(url))

    page = requests.get(url)
    data = page.text

    result = re.search(
        r"var gallery = \[\{name: \'products\',files: \[\{(.*?)\}\]", data
    )

    print("Scraping completed!\n")

    if result:
        return [product_from_text(p, url) for p in result.group(1).split(r"},{ ")]

    return None
