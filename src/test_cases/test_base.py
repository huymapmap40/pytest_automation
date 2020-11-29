import pytest
from src.wrappers.browser_wrapper import BrowserWrapper


@pytest.mark.usefixtures("setup_driver")
class TestBase:
    
    browser_obj = None
    
    def setup_method(self):
        print("Setup")
        global browser_obj
        browser_obj = BrowserWrapper()
        browser_obj.maximize_window_browser()

    def teardown_method(self):
        print("Teardown")
        # browser_obj.close()
        
    def navigate_to(self, url):
        browser_obj.go_to_url(url)
