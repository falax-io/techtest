
class IndexPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("xpath=.//input[@id='user-name']")
        self.password_input = page.locator("xpath=.//input[@id='password' and @type='password']")
        self.login_input = page.locator("xpath=.//input[@id='login-button' and @type='submit']")
        self.error_button = page.locator("xpath=.//h3[@data-test='error']/button[@class='error-button']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_input.click()

    def is_error_displayed(self):
        return self.error_button.is_visible()
