import toasts.toast_messages
from pages.base_page import BasePage
from locators import base_page_locator
from time import sleep


# from toasts.toast_messages import AuthPageToasts
SLEEP_AFTER_ACTION = 0.5
LONG_SLEEP_WAIT = 2.5


class SignUpPage(BasePage):
    def __init__(self, driver, creds=None):
        super().__init__(driver)
        self.signup_locator = base_page_locator.StartPageLocators.GO_TO_SIGNUP
        if creds:
            self.email, self.password, self.name = creds
        else:
            # TODO: Пользователя задавать через параметр функции
            self.email, self.password, self.name = self.get_creds('user3')

    def go_to_signup_page(self):
        self.click_element(self.signup_locator)

    def set_email(self):
        self.email, mail_class = self.get_available_domains(self.email, self.password)
        return mail_class

    def send_name(self):
        name_locator = base_page_locator.SignUpLocators.NAME_FORM
        self.send_info(name_locator, self.name)

    def send_email(self):
        email_locator = base_page_locator.SignUpLocators.EMAIL_FORM
        self.send_info(email_locator, self.email)

    def send_pass(self, locator):
        self.send_info(locator, self.password)

    def enter_pass_and_second(self):
        pass_locator = base_page_locator.SignUpLocators.PASSWORD_FORM
        repeat_pass_locator = base_page_locator.SignUpLocators.SECOND_PASSWORD_FORM
        self.send_pass(pass_locator)
        self.send_pass(repeat_pass_locator)

    def send_code(self, mail, email_address, wrong_code=None):
        if wrong_code:
            code = wrong_code
        else:
            code = str(self.get_code(mail, email_address))
        code_locator = base_page_locator.SignUpLocators.CODE_FORM
        self.send_info(code_locator, code)

    def click_checkbox(self):
        checkbox_locator = base_page_locator.SignUpLocators.LICENCE_BOX
        self.click_element(checkbox_locator)

    def registration(self, inc_name=bool, inc_email=bool, inc_pass=bool, inc_code=bool):
        self.go_to_signup_page()
        mail_class = self.set_email()
        self.send_name()
        self.send_email()
        self.click_proceed_btn()
        self.send_code(mail_class, self.email)
        sleep(SLEEP_AFTER_ACTION)
        # Принять соглашение и нажать далее
        self.click_checkbox()
        sleep(SLEEP_AFTER_ACTION)
        self.click_proceed_btn()
        sleep(SLEEP_AFTER_ACTION*2)
        # Ввести пароль и повторить
        self.enter_pass_and_second()
        print(self.password)
        sleep(SLEEP_AFTER_ACTION)
        # Нажать далее
        self.click_proceed_btn()
        sleep(LONG_SLEEP_WAIT)
