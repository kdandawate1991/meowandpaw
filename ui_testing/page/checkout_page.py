from ui_testing.page.base_page import BasePage


class CheckoutProcess(BasePage):
    CHECKOUT = '[data-test="checkout"]'
    FIRST_NAME = '[data-test="firstName"]'
    LAST_NAME = '[data-test="lastName"]'
    POSTAL_CODE = '[data-test="postalCode"]'
    CONTINUE_BUTTON = '[data-test="continue"]'
    FINISH_BUTTON = '[data-test="finish"]'
    FINAL_PAGE = '.complete-header'

    def __init__(self, page):
        super().__init__(page)

    def checkout(self):
        self.page.click(self.CHECKOUT)

    def fill_form(self, first_name, last_name, postal_code):
        """:param first_name: string: first name of buyer
           :param last_name: string: last name of buyer
           :param postal_code: string: postal code of byer
        """
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)

    def complete_checkout(self):
        self.page.click(self.CONTINUE_BUTTON)
        self.page.click(self.FINISH_BUTTON)
        thank_you_text = self.page.text_content(self.FINAL_PAGE)
        assert "Thank you for your order!" == thank_you_text

