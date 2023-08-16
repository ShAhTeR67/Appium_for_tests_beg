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
    GO_TO_LOGIN = (By.ID, 'io.fasthome.sls:id/go_login')
    LOGO_ICON = (By.ID, 'io.fasthome.sls:id/logo')
    CODE_FORM = (By.ID, 'io.fasthome.sls:id/e_access_code')
    LICENCE_BOX = (By.ID, 'io.fasthome.sls:id/checkBox_agreement')
    AGREEMENT_DOC = (By.ID, 'io.fasthome.sls:id/tv_agreement_familiarize')
    CODE_INFO_MSG = (By.ID, 'io.fasthome.sls:id/tv_info_code')


