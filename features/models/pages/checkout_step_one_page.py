class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page
        self.continue_input = page.locator("xpath=.//input[@id='continue']")
        self.first_name_input = page.locator("xpath=.//input[@id='first-name']")
        self.last_name_input = page.locator("xpath=.//input[@id='last-name']")
        self.postal_code_input = page.locator("xpath=.//input[@id='postal-code']")

    def fill_the_form(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def click_continue(self):
        self.continue_input.click()

