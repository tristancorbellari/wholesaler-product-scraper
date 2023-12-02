import util.constants as c


class Product():
    def __init__(self, site_category, image_url, code, title, price, description):
        self.site_category = site_category
        self.image_url = image_url
        self.code = code
        self.title = title
        self.price = price
        self.description = description
        self.collection = ""
        self.vendor = c.VENDOR
        self.weight = ""
        self.weight_unit = c.DEFAULT_WEIGHT_UNIT
        self.status = c.DEFAULT_STATUS