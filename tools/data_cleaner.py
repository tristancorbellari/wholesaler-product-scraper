import re
import util.constants as c
import util.operations as o


def clean_cardstock(data):
    print("Cleaning Cardstock...")

    # Don't include any AC cardstock, i.e. product code starts with "AC"
    data = [p for p in data if not p["Code"].startswith("AC")]

    for d in data:
        d["Body (HTML)"] = c.CARDSTOCK_DESCRIPTION
        d["Collection"] = c.CARDSTOCK_COLLECTION
        d["Price"] = c.CARDSTOCK_PRICE

        # Where title contains something like "(216gsm, 10 Sheets)", remove it from title and set product weight
        title_quantities_match = re.search(r"\((\d*)(\w*), \d+ Sheets\)", d["Title"])
        if title_quantities_match:
            if title_quantities_match.group(2) == "gsm":
                d["Weight Unit"] = "g"
            d["Weight"] = (
                title_quantities_match.group(1)
                if title_quantities_match.group(1) is not None
                else ""
            )

            d["Title"] = d["Title"][: (title_quantities_match.start())]

    return data


def clean_chalk_ink(data):
    print("Cleaning Chalk Ink...")

    for d in data:
        d["Body (HTML)"] = c.CHALK_INK_DESCRIPTION
        d["Collection"] = c.CHALK_INK_COLLECTION
        d["Price"] = c.CHALK_INK_PRICE

    return data


def clean_flowers(data):
    print("Cleaning Flowers...")

    # Don't include any bulk packs, i.e. product code starts with "BULK"
    data = [p for p in data if not p["Code"].startswith("BULK")]

    for d in data:
        d["Body (HTML)"] = c.FLOWERS_DESCRIPTION
        d["Collection"] = c.FLOWERS_COLLECTION

    return data


def clean_strings(data):
    print("Cleaning strings...")
    for d in data:
        for key, value in d.items():
            d[key] = re.sub(r"( *[^A-Za-z0-9\.\)]* *)$", "", value)
            d[key] = value.replace("&amp;", "&")

    return data


def clean_data(data):
    print("Starting data cleaning...")

    if data[0]["Site Category"] == o.end_of_url(c.CARDSTOCK_URL):
        data = clean_cardstock(data)
    elif data[0]["Site Category"] == o.end_of_url(c.CHALK_INK_URL):
        data = clean_chalk_ink(data)
    elif data[0]["Site Category"] == o.end_of_url(c.FLOWERS_URL):
        data = clean_flowers(data)

    data = clean_strings(data)

    print("Data cleaning completed!\n")

    return data
