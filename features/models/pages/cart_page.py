class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("xpath=.//button[@id='checkout']")

    def click_checkout(self):
        self.checkout_button.click()
