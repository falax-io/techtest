class CheckoutStepTwoPage:
    def __init__(self, page):
        self.page = page
        self.continue_input = page.locator("xpath=.//button[@id='finish']")
        self.total_div = page.locator("xpath=.//div[@class='summary_info_label summary_total_label']")

    def click_finish(self):
        self.continue_input.click()

    def get_total_dollars(self):
        return self.total_div.text_content()
