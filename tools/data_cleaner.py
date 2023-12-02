import re
import util.constants as c


def clean_cardstock(data):
    for d in data:
        d["Body (HTML)"] = c.CARDSTOCK_DESCRIPTION

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

        d["Collection"] = c.CARDSTOCK_COLLECTION
        d["Price"] = c.CARDSTOCK_PRICE

        # Don't include any AC cardstock, i.e. product code starts with "AC"
        data = [p for p in data if not p["Code"].startswith("AC")]

    return data


def clean_chalk_ink(data):
    return data


def clean_flowers(data):
    return data


def remove_trailing_spaces(data):
    for d in data:
        for key, value in d.items():
            if key != "Price":
                d[key] = re.sub(r"( *[^A-Za-z0-9\.\)]* *)$", "", value)

    return data


def clean_data(data):
    data = clean_cardstock(data)
    data = clean_chalk_ink(data)
    data = clean_flowers(data)

    data = remove_trailing_spaces(data)
    return data
