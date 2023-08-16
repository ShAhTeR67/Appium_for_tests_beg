from time import sleep

import toasts.toast_messages
from pages.base_page import BasePage
from locators import base_page_locator
from toasts.toast_messages import LogInPageToasts


class LoginPage(BasePage):
    def __init__(self, driver, creds=None):
        super().__init__(driver)
        self.login_locator = base_page_locator.StartPageLocators.GO_TO_LOGIN
        if creds:
            self.email, self.password, self.name = creds
        else:
            self.email, self.password, self.name = self.get_creds('user1')

    def login(self):
        self.go_to_login_page()
        self.send_email()
        self.send_password()
        self.click_proceed_btn()

    def go_to_login_page(self):
        self.click_element(self.login_locator)

    def send_email(self):
        email_locator = base_page_locator.LogInLocators.EMAIL_FORM
        self.send_info(email_locator, self.email)

    def send_password(self):
        password_locator = base_page_locator.LogInLocators.PASSWORD_FORM
        self.send_info(password_locator, self.password)

    def get_toast(self, cor_toast_msg):
        toast_pointer = base_page_locator.TOAST
        toast_msg = cor_toast_msg
        toast = self.get_toast_message(toast_pointer)
        assert toast == toast_msg, \
            f'Тосты не совпадают. Ожидалось - "{toast_msg}", а получили "{toast}"'
        return toast

    def get_empty_email_toast(self):
        toast_msg = LogInPageToasts.EMPTY_EMAIL
        toast = self.get_toast(toast_msg)
        return toast

    def get_empty_password_toast(self):
        toast_msg = LogInPageToasts.EMPTY_PASSWORD
        toast = self.get_toast(toast_msg)
        return toast

    def get_wrong_creds_toast(self):
        toast_msg = LogInPageToasts.WRONG_CREDS
        toast = self.get_toast(toast_msg)
        return toast

    def get_no_internet_toast(self):
        toast_msg = LogInPageToasts.NO_INTERNET_CONNECTION
        toast = self.get_toast(toast_msg)
        return toast

    # По идеи должна быть в base_page.py
    def get_timeout_toast(self):
        toast_msg = LogInPageToasts.TIMEOUT_ERR
        toast = self.get_toast(toast_msg)
        return toast

    # def is_empty_password_toast_present(self):
    #     toast_pointer = base_page_locator.TOAST
    #     empty_toast_msg = LogInPageToasts.EMPTY_PASSWORD
    #     toast = self.get_toast_message(toast_pointer)
    #     assert toast == empty_toast_msg, \
    #         f'Тосты не совпадают. Ожидалось - {empty_toast_msg}, а получили {toast}'
    #
    # def is_wrong_creds_toast_present(self):
    #     toast_pointer = base_page_locator.TOAST
    #     wrong_creds_toast_msg = LogInPageToasts.WRONG_CREDS
    #     toast = self.get_toast_message(toast_pointer)
    #     assert toast == wrong_creds_toast_msg, \
    #         f'Тосты не совпадают. Ожидалось - {wrong_creds_toast_msg}, а получили {toast}'

    def set_email(self, new_email):
        self.email = new_email

    def set_password(self, new_password):
        self.password = new_password

    def get_password(self):
        hide_pass_btn_locator = base_page_locator.LogInLocators.HIDE_PASS_BUTTON
        password_locator = base_page_locator.LogInLocators.PASSWORD_FORM
        self.click_element(hide_pass_btn_locator)
        password = self.get_info(password_locator)
        return password

    def clear_email(self, pointer):
        pass

# TODO: так как тосты получаются во всем приложении, то и get_toast должен быть перенес туда
