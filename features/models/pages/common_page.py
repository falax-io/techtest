class CommonPage:
    def __init__(self, page):
        self.page = page
        self.burger_menu_button = page.locator("xpath=.//button[@id='react-burger-menu-btn']")
        self.logout_lnk = page.locator("xpath=.//a[@id='logout_sidebar_link']")

    def click_hamburger_menu(self):
        self.burger_menu_button.click()

    def click_logout(self):
        self.logout_lnk.click()
