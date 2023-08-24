import time
import pytest
import base64
import testit

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from Credentials.creds import creds_from_json


@testit.workItemIds(433)
@testit.displayName('Авторизация')
@pytest.mark.release_authorization
class TestLoginPage:
    def test_valid_logon(self, mobile_driver):
        main_page = LoginPage(mobile_driver)
        main_page.login()
        main_page.is_toast_missing()
        time.sleep(0.2)
        screenshot = mobile_driver.get_screenshot_as_base64()
        with open('my_image.png', 'wb') as file:
            file.write(base64.b64decode(screenshot))
        # take_screenshot() - not implemented yet

    def test_wrong_password(self, mobile_driver):
        main_page = LoginPage(mobile_driver, ['testtttt2022@mail.ru', 'wrong', 'name'])
        main_page.login()
        toast = main_page.get_wrong_creds_toast()
        if not toast:
            return False

    def test_invalid_symbols_in_password(self, mobile_driver):
        main_page = LoginPage(mobile_driver, ['testtttt2022@mail.ru', 'ㅤ ×÷|¥₩₽©℗™°😁😂🤣⅔½↘↗ćÇ€1', 'name'])
        main_page.go_to_login_page()
        main_page.send_email()
        main_page.send_password()
        time.sleep(0.5)
        password = main_page.get_password()
        if not password:
            return False
        assert password == '1', f"Passwords doesn't match/nExpected '1' but got {password}"

    def test_wrong_email(self, mobile_driver):
        main_page = LoginPage(mobile_driver, ['testtttttttt2022@mail.ru', 'testsls2022', 'name'])
        main_page.login()
        time.sleep(0.5)
        toast = main_page.get_wrong_creds_toast()
        if not toast:
            return False

    @pytest.mark.skip('The same as test_wrong_email')
    def test_invalid_email_format(self, mobile_driver):
        main_page = LoginPage(mobile_driver, ['testtttttttt2022@mail.ru', 'testsls2022', 'name'])
        main_page.login()
        time.sleep(0.5)
        toast = main_page.get_wrong_creds_toast()
        if not toast:
            return False

    def test_empty_email_field(self, mobile_driver):
        main_page = LoginPage(mobile_driver, ['', 'wrong', 'name'])
        main_page.go_to_login_page()
        main_page.send_password()
        time.sleep(0.2)
        main_page.click_proceed_btn()
        time.sleep(0.2)
        toast = main_page.get_empty_email_toast()
        if not toast:
            return False

    def test_empty_password_field(self, mobile_driver):
        main_page = LoginPage(mobile_driver)
        main_page.go_to_login_page()
        main_page.send_email()
        time.sleep(0.2)
        main_page.click_proceed_btn()
        time.sleep(0.2)
        toast = main_page.get_empty_password_toast()
        if not toast:
            return False

    @pytest.mark.skip('The same as empty email')
    def test_empty_obligatory_fields(self, mobile_driver):
        main_page = LoginPage(mobile_driver)
        main_page.go_to_login_page()
        main_page.send_password()
        time.sleep(0.5)
        main_page.click_proceed_btn()
        toast = main_page.get_empty_email_toast()
        if not toast:
            return False

    def test_auth_without_internet_connection(self, mobile_driver):
        mobile_driver.set_network_connection(0)
        main_page = LoginPage(mobile_driver)
        main_page.login()
        time.sleep(0.5)
        toast = main_page.get_no_internet_toast()
        if not toast:
            return False

    @pytest.mark.skip
    # Еще не проверял на работоспособность
    def test_timeouts(self, mobile_driver):
        main_page = LoginPage(mobile_driver)
        main_page.go_to_login_page()
        for i in range(30):
            main_page.click_proceed_btn()
            toast = main_page.get_timeout_toast()
        if not toast:
            return False


@testit.workItemIds(432)
@testit.displayName('Регистрация')
@pytest.mark.release_registration
class TestSignupPage:
    # Skip. Not done yet
    # def test_spam_protection(self, mobile_driver):
    #     page = SignUpPage(mobile_driver)
    #     page.go_to_signup_page()
    #     time.sleep(6000)

    def test_enter_correct_creds(self, mobile_driver):
        user = creds_from_json('user3')
        page = SignUpPage(mobile_driver, user)
        page.registration()

    def test_exists_user_email(self, mobile_driver):
        self.test_enter_correct_creds(mobile_driver)

    def test_enter_incorrect_creds(self, mobile_driver):
        user = creds_from_json('user3')
        user[0], user[2] = '.u@se#$', 'Имя Ф@miл1я'
        page = SignUpPage(mobile_driver, user)
        page.registration()

    def test_no_email_registration(self, mobile_driver):
        user = creds_from_json('user3')
        user[0] = ''
        page = SignUpPage(mobile_driver, user)
        page.registration()

    def test_no_name_registration(self, mobile_driver):
        user = creds_from_json('user3')
        user[0], user[2] = '', ''
        page = SignUpPage(mobile_driver, user)
        page.registration()

    def test_no_password_registration(self, mobile_driver):
        user = creds_from_json('user3')
        user[1] = ''
        page = SignUpPage(mobile_driver, user)
        page.registration()

    def test_incorrect_verification_code(self, mobile_driver):
        user = creds_from_json('user3')
        incorrect_code = 111111
        page = SignUpPage(mobile_driver, user)
        page.go_to_signup_page()
        email_class = page.set_email()
        page.send_name()
        page.send_email()
        page.click_proceed_btn()
        page.send_code(email_class, page.email, incorrect_code)
        page.click_checkbox()
        page.click_proceed_btn()
        # TODO: Нехватает проверок строки ошибки. Тест без нее будет падать

    def test_empty_code(self):
        pass

    def test_empty_pass_fields(self, mobile_driver):
        pass

    def test_incorrect_repeat_password(self, mobile_driver):
        pass

    def test_empty_repeat_password(self, mobile_driver):
        pass

    def test_no_user_policy(self, mobile_driver):
        pass


@testit.workItemIds(431)
@testit.displayName('Подготовка')
@pytest.mark.skip(reason="not implemented yet")
# @pytest.mark.release_first_start
class TestFirstLaunch:
    def test_main_page(self, mobile_driver):
        home_page = BasePage(mobile_driver)
        home_page.open_page()
        time.sleep(5)

    def test_demo(self, mobile_driver):
        home_page = BasePage(mobile_driver)
        home_page.open_demo()
        time.sleep(5)

    def test_signup_page(self, mobile_driver):
        home_page = BasePage(mobile_driver)
        home_page.open_signup_page()
        time.sleep(5)


# TODO: Создать парсер JSON и через него подключать аккаунты
# TODO: Реализовать нормально ООП
# TODO: Реализовать нормальные функции
# TODO: В идеале тесты на вход можно внести в одну функцию, меняя параметры входа
# TODO: Есть проблемы с паузами
# TODO: Обрабатывать текствью ошибки (пустое поле)