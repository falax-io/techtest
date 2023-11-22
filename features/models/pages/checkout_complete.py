class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self.success_message_h2 = page.locator("xpath=.//h2[@class='complete-header']")
        self.success_img = page.locator("xpath=.//img[@class='pony_express']")

    def is_checkout_complete(self):
        return self.success_message_h2.is_visible() and self.success_img.is_visible()


