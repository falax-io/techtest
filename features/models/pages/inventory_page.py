def get_inventory_item_xpath(item_name):
    return "xpath=.//div[@class='inventory_item']//div[text()='" + item_name + "']/../../../../"


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.shopping_cart_lnk = page.locator("xpath=.//a[@class='shopping_cart_link']")

    def add_item_to_cart(self, item_name):
        self.page.locator(get_inventory_item_xpath(item_name) + ".//button").click()

    def click_cart(self):
        self.shopping_cart_lnk.click()
