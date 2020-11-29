import json
import collections
from os import path
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from src.utilities.driver_constant import DriverConstant
from selenium.webdriver.android.webdriver import WebDriver as AndroidWebDriver


class DriverManagement:

    __instance = None

    @staticmethod
    def get_instance():
        if DriverManagement.__instance is None:
            DriverManagement.__instance = DriverManagement()
        return DriverManagement.__instance

    def init_driver(self, **kwargs):
        config_dir = path.dirname(path.dirname(__file__))
        with open(path.join(config_dir, 'config_env_test.json')) as f:
            data_setup = json.load(f)
            initial_driver = None
            browser_name = kwargs["browser_name"]
            if data_setup['config_info']['enable_remote_webdriver']:
                remote_address = data_setup['remote_webdriver']['remote_address']
                desired_capabilities = {"browserName": browser_name, "platform": "ANY"}
                initial_driver = webdriver.Remote(command_executor=remote_address, desired_capabilities=desired_capabilities)
            else:
                if browser_name == DriverConstant.CHROME_BROWSER:
                    initial_driver = webdriver.Chrome(executable_path=path.abspath("src/drivers/chromedriver.exe"))
                elif browser_name == DriverConstant.FIREFOX_BROWSER:
                    initial_driver = webdriver.Firefox(executable_path=path.abspath("src/drivers/geckodriver.exe"))
                else:
                    raise KeyError("Browser name not found!")
            initial_wait = WebDriverWait(initial_driver, DriverConstant.DRIVER_TIMEOUT)
            web_browser_init = collections.namedtuple('WebInit', ['Driver', 'Wait'])
            return web_browser_init(initial_driver, initial_wait)
                    