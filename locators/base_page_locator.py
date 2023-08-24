from selenium.webdriver.common.by import By

TOAST = (By.ID, 'io.fasthome.sls:id/snackbar_text')
# The same for login and registration pages
PROCEED_BUTTON = (By.ID, 'io.fasthome.sls:id/btn_next')


class StartPageLocators:
    GO_TO_SIGNUP = (By.ID, 'io.fasthome.sls:id/go_signup')
    GO_TO_LOGIN = (By.ID, 'io.fasthome.sls:id/go_login')
    GO_TO_DEMO = (By.ID, 'io.fasthome.sls:id/demo')
    LOGO_ICON = (By.ID, 'io.fasthome.sls:id/lottie')


class LogInLocators:
    EMAIL_FORM = (By.ID, 'io.fasthome.sls:id/e_name')
    PASSWORD_FORM = (By.ID, 'io.fasthome.sls:id/e_password')
    RESET_PASSWORD_BUTTON = (By.ID, 'io.fasthome.sls:id/forgot_password')
    GO_TO_REGISTRATION = (By.ID, 'io.fasthome.sls:id/go_signup')
    LOGO_ICON = (By.ID, 'io.fasthome.sls:id/logo')
    HIDE_PASS_BUTTON = (By.ID, 'io.fasthome.sls:id/showhidepass')
    ACCEPT_GEO = (By.ID, 'io.fasthome.sls:id/btn_accept')
    GEO_ACCESS_TYPE = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')


class SignUpLocators:
    NAME_FORM = (By.ID, 'io.fasthome.sls:id/e_name')
    EMAIL_FORM = (By.ID, 'io.fasthome.sls:id/e_email')
    PASSWORD_FORM = (By.ID, 'io.fasthome.sls:id/e_password')
    SECOND_PASSWORD_FORM = (By.ID, 'io.fasthome.sls:id/e_second_pass')
    # Если в первом поле нет данных, то второе должно быть заблокировано
    # Параметр enabled у него должен быть false
    GO_TO_LOGIN = (By.ID, 'io.fasthome.sls:id/go_login')
    LOGO_ICON = (By.ID, 'io.fasthome.sls:id/logo')
    CODE_FORM = (By.ID, 'io.fasthome.sls:id/e_access_code')
    LICENCE_BOX = (By.ID, 'io.fasthome.sls:id/checkBox_agreement')
    AGREEMENT_DOC = (By.ID, 'io.fasthome.sls:id/tv_agreement_familiarize')
    CODE_INFO_MSG = (By.ID, 'io.fasthome.sls:id/tv_info_code')
    NAME_STRING = (By.ID, 'io.fasthome.sls:id/tv_name')
    # Пример поля text строки имя "Добрый день, {user_name}!"
    LICENCE_DISPLAY = (By.ID, 'io.fasthome.sls:id/bottom_sheet_agreement_policy')
    # У экрана лицензии должны быть два параметра enabled и displayed в значении true
    # Для выхода назад нажимать кнопку "Назад"
    PASSWORD_LEVEL = (By.ID, 'io.fasthome.sls:id/tv_pass_level')
    # Проверка сложности пароля. Слабые пароля не должны приниматься
    # Строка сложности располагается в параметре text пр "Очень слабый"
    # Отображается только после ввода первичного пароля
    WRONG_SECOND_PASSWORD = (By.ID, 'io.fasthome.sls:id/tv_pass_error')
    # Если введен неправильный пароль отобразится интекствью ошибка
    # В поле text значение "Введенные пароли не совпадают"
    SHOW_PASSWORD_BTN = (By.ID, 'io.fasthome.sls:id/btn_show_hide_pass')
    SHOW_SECOND_PASSWORD_BTN = (By.ID, 'io.fasthome.sls:id/btn_second_showhidepass')
    NAME_FIELD_ERR = (By.ID, 'io.fasthome.sls:id/tv_error_name')
    # Text Имя не может быть пустым
    EMAIL_FIELD_ERR = (By.ID, 'io.fasthome.sls:id/tv_error_email')
    # Text Эл. почта не может быть пустой / Недопустимый формат электронной почты


