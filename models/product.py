import util.constants as c


class Product:
    def __init__(self, site_category, image_url, code, title, price, description):
        self["Site Category"] = site_category
        self["Image Src"] = image_url
        self["Code"] = code
        self["Title"] = title
        self["Price"] = price
        self["Body (HTML)"] = description
        self["Collection"] = ""
        self["Vendor"] = c.VENDOR
        self["Weight"] = ""
        self["Weight Unit"] = c.DEFAULT_WEIGHT_UNIT
        self["Status"] = c.DEFAULT_STATUS

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n".format(
            self["Site Category"],
            self["Image Src"],
            self["Code"],
            self["Title"],
            self["Price"],
            self["Body (HTML)"],
            self["Collection"],
            self["Vendor"],
            self["Weight"],
            self["Weight Unit"],
            self["Status"],
        )

    def items(self):
        return [(v, getattr(self, v)) for v in vars(self)]
