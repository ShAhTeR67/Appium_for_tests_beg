import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from Credentials import creds
from locators import base_page_locator
from temp_mail.mail import TempMail

SLEEP_TIME = 10
SLEEP_AFTER_ACTION = 0.4


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Wait app to load for 5 sec
        self.driver_wait = SLEEP_TIME
        self.proceed_button = base_page_locator.PROCEED_BUTTON

    def is_clickable(self, pointer: tuple):
        return WebDriverWait(self.driver, self.driver_wait).until(EC.element_to_be_clickable(pointer))

    def is_element_present(self, pointer: tuple):
        return WebDriverWait(self.driver, self.driver_wait).until(EC.presence_of_element_located(pointer))

    def click_element(self, pointer: tuple):
        element = self.is_clickable(pointer)
        time.sleep(SLEEP_AFTER_ACTION)
        element.click()
        time.sleep(SLEEP_AFTER_ACTION)

    def send_info(self, pointer: tuple, message: str):
        field = self.is_element_present(pointer)
        field.send_keys(message)
        time.sleep(SLEEP_AFTER_ACTION)

    @staticmethod
    def get_creds(user_name: str):
        return list(creds.creds_from_json(user_name))

    def is_toast_present(self, pointer: tuple):
        try:
            toast = self.is_element_present(pointer)
            if toast:
                return toast
            else:
                return False
        except TE:
            return False

    def is_toast_missing(self):
        toast_pointer = base_page_locator.TOAST
        toast = self.is_toast_present(toast_pointer)
        assert not toast, f'Присутствует тост, хотя не должен. Содержимое "{toast}"'

    def get_toast_message(self, pointer: tuple):
        toast = self.is_toast_present(pointer)
        if not toast:
            return "Toast wasn't found"
        return toast.text

    def get_info(self, pointer):
        field = self.is_element_present(pointer)
        if not field:
            return False
        return field.text

    def click_proceed_btn(self):
        self.click_element(self.proceed_button)

    @staticmethod
    def create_email(email):
        # Автоматизировать ввод доменного имени
        # email.get_domains(email_address)
        creation = email.post_create_account()
        if creation == 201:
            email.post_auth()
        else:
            return creation

    @staticmethod
    def is_email_created(email) -> bool:
        is_created = False
        if email.post_auth():
            is_created = True
        return is_created

    def get_code(self, mail, email_address) -> int:
        email = mail
        check = self.is_email_created(email)
        time.sleep(SLEEP_AFTER_ACTION)
        if not check:
            self.create_email(email)
        time.sleep(SLEEP_TIME)
        email.get_messages()
        time.sleep(SLEEP_AFTER_ACTION)
        code = email.parse_message()
        return code

    @staticmethod
    def get_available_domains(email_address, password):
        temp_email_class = TempMail(email_address, password=password)
        full_email = temp_email_class.email
        return [full_email, temp_email_class]


    # def open_demo(self):
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(base_page_locator.StartPageLocators.
    #                                                                     GO_TO_DEMO)).click()
    # def fill_registration_form(self):
    #     WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(base_page_locator.RegisterLocators.
    #                                                                        EMAIL_FORM)).send_keys()
    # def open_signup_page(self):
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(base_page_locator.StartPageLocators.
    #                                                                     GO_TO_SIGNUP)).click()

# TODO: Реализовать функцию take_screenshot
# TODO: Изменить проверку кнопок. Недостаточно проверять возможность нажать на элемент. Необходимо так же проверить,
#  что кнопка существует (present)
