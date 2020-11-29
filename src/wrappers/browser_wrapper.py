from src.utilities.driver_constant import DriverConstant
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, JavascriptException
from src.config.setup.driver_management import DriverManagement
from selenium import webdriver


class BrowserWrapper:
    # webdriver.Firefox().get_screenshot_as_png()
    __currentBrowserDriver: WebDriver = None

    @staticmethod
    def instance_driver() -> WebDriver:
        return BrowserWrapper.__currentBrowserDriver

    # Set web driver instance
    @staticmethod
    def inject_driver(driver):
        try:
            if BrowserWrapper.__currentBrowserDriver is None:
                BrowserWrapper.__currentBrowserDriver = driver
        except:
            raise WebDriverException("Web driver has not been init")

    def set_page_load_timeout(self, timeout_in_second):
        BrowserWrapper.instance_driver().set_page_load_timeout(timeout_in_second)

    def set_element_timeout(self, timeout_in_second):
        BrowserWrapper.instance_driver().implicitly_wait(timeout_in_second)

    def maximize_window_browser(self):
        BrowserWrapper.instance_driver().maximize_window()

    def go_to_url(self, url):
        current_driver = BrowserWrapper.instance_driver()
        current_driver.get(url)
        WebDriverWait(current_driver, DriverConstant.DRIVER_TIMEOUT).until(
            lambda x: x.execute_script("return document.readyState") == "complete")
        self.set_page_load_timeout(DriverConstant.PAGE_LOAD_TIMEOUT)
        self.set_element_timeout(DriverConstant.ELEMENT_TIMEOUT)

    def get_screenshot_png(self):
        return BrowserWrapper.instance_driver().get_screenshot_as_png()

    @staticmethod
    def is_alert_displayed():
        wait = WebDriverWait(BrowserWrapper.instance_driver(), DriverConstant.MIDDLE_TIMEOUT)
        return False if wait.until(EC.alert_is_present()) is None else True

    @staticmethod
    def accept_alert():
        BrowserWrapper.instance_driver().switch_to.alert.accept()

    @staticmethod
    def cancel_alert():
        BrowserWrapper.instance_driver().switch_to.alert.dismiss()

    @staticmethod
    def execute_javascript(script_string, *args):
        try:
            return BrowserWrapper.instance_driver().execute_script(script_string, args)
        except:
            raise JavascriptException("Could not execute the script '{}'".format(script_string))

    @staticmethod
    def refresh_page():
        BrowserWrapper.instance_driver().refresh()

    def close(self):
        BrowserWrapper.instance_driver().close()
