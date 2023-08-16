import os

import pytest
from appium import webdriver


ANDROID_BASE_CAPS = {
    'app': os.path.abspath('../apps/app-release.apk'),
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '12.0',
    'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'Android emulator',
    'newCommandTimeOut': '1800'
}


# Set up webdriver fixture
@pytest.fixture(scope='function')
def mobile_driver(request):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', ANDROID_BASE_CAPS)
    driver.set_network_connection(6)
    print('\nDriver instance is created')

    def quit_driver():
        driver.quit()
        print('\nDriver instance is closed')

    request.addfinalizer(quit_driver)
    return driver


# TODO: Исправить логи с print на полноценное логирование (по всем модулям)