from __future__ import annotations
from assertpy import assert_that
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from src.wrappers.element_wrapper import ElementWrapper
from src.wrappers.browser_wrapper import BrowserWrapper
from .search_weather_result_page import SearchWeatherResultPage


class OpenWeatherHomePage:
    
    __instance: OpenWeatherHomePage = None
    _inp_city_name = ElementWrapper((By.CSS_SELECTOR, "#q"))

    @staticmethod
    def get_instance():
        if OpenWeatherHomePage.__instance == None:
            OpenWeatherHomePage.__instance = OpenWeatherHomePage()
        return OpenWeatherHomePage.__instance
    
    def search_weather_in_your_city(self, city_value) -> SearchWeatherResultPage:
        self._inp_city_name.type(city_value)
        self._inp_city_name.press_key(Keys.ENTER)
        return SearchWeatherResultPage.get_instance()
    
    def verify_open_weather_home_page_is_displayed(self):
        assert_that(self._inp_city_name.is_element_displayed()).is_true()
