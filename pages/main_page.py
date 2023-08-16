# The main page of the app
# after authentication
from base_page import BasePage
from locators import base_page_locator


class MainPage(BasePage):
    def __init__(self):
        super(MainPage, self).__init__()
