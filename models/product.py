import util.constants as c


class Product:
    def __init__(self, site_category, image_url, code, title, price, description):
        self["Site Category"] = site_category
        self["Image Src"] = image_url
        self["Code"] = code
        self["Title"] = title
        self["Price"] = str(price)
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
        res = ""
        for item in self.items():
            res += str(item[0]) + ": " + str(item[1]) + "\n"

        return res

    def __iter__(self):
        return iter([getattr(self, v) for v in vars(self)])

    def items(self):
        return [[v, getattr(self, v)] for v in vars(self)]
    
    def keys(self):
        return [v for v in vars(self)]
