class BasePage:
    def __init__(self, page):
        self.page = page

    def login_to_saucedemo(self):
        self.page.goto('https://www.saucedemo.com/')
        self.page.fill('input[data-test="username"]', 'standard_user')
        self.page.fill('input[data-test="password"]', 'secret_sauce')
        self.page.click('input[data-test="login-button"]')
