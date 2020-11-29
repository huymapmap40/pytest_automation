from __future__ import annotations
import math
import re
from unicodedata import normalize
from assertpy import assert_that, soft_assertions
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from src.wrappers.element_wrapper import ElementWrapper
from src.wrappers.browser_wrapper import BrowserWrapper
from src.apis.helpers.current_weather_helper import CurrentWeatherHelper
from src.data.pages.open_weather_result import OpenWeatherResultData


class SearchWeatherResultPage:
    
    __instance = None
    _lbl_header_title = ElementWrapper((By.XPATH, '//h2[@class="headline first-child text-color"]'))
    _txt_search_string = ElementWrapper((By.CSS_SELECTOR, "#search_str"))
    _btn_search = ElementWrapper((By.XPATH, '//button[@type="submit"]'))
    _tbl_forecast_list = ElementWrapper((By.CSS_SELECTOR, "#forecast-list"))
    _lbl_guideline_title = ElementWrapper((By.CSS_SELECTOR, ".col-sm-12 h3"))
    _lbl_guideline_content = ElementWrapper((By.CSS_SELECTOR, ".col-sm-12 ul li"))
    _pnl_not_found = ElementWrapper((By.CSS_SELECTOR, ".alert.alert-warning"))
    
    # Dynamic controls
    def _weather_result_row(self, index):
        table_weather_result_locator = "//div[@id='forecast-list']"
        return { 
                 "txt_city_name" : ElementWrapper((By.XPATH, f"{table_weather_result_locator}//tr[{index}]/td[2]/b/a")),
                 "txt_description": ElementWrapper((By.XPATH, f"{table_weather_result_locator}//tr[{index}]/td[2]/b[2]")),
                 "span_temperature": ElementWrapper((By.XPATH, f"{table_weather_result_locator}//tr[{index}]/td[2]//span")),
                 "txt_weather_detail_content": ElementWrapper((By.XPATH, f"{table_weather_result_locator}//tr[{index}]/td[2]/p[1]")),
                 "txt_coordinate": ElementWrapper((By.XPATH, f"{table_weather_result_locator}//tr[{index}]/td[2]/p/a"))
            }

    @staticmethod
    def get_instance():
        if SearchWeatherResultPage.__instance == None:
            SearchWeatherResultPage.__instance = SearchWeatherResultPage()
        return SearchWeatherResultPage.__instance

    def verify_ui_result_page_is_displayed_correctly(self):
        assert_that(self._lbl_header_title.get_text()).is_equal_to(OpenWeatherResultData.HEADER_TITLE)
        assert_that(self._btn_search.is_element_displayed()).is_true()
        assert_that(self._txt_search_string.is_element_displayed()).is_true()
        assert_that(self._lbl_guideline_title.get_text()).is_equal_to(OpenWeatherResultData.GUIDELINE_TITLE)
        assert_that(self._lbl_guideline_content.get_text()).is_equal_to(OpenWeatherResultData.GUIDELINE_CONTENT)

    def verify_search_data_weather_result_is_correctly(self, city_name):
        expect_current_weather = CurrentWeatherHelper.get_current_weather_by_city(city_name).json()
        actual_weather_data = self._weather_result_row(index=1)
        with soft_assertions():
            assert_that(self._txt_search_string.get_attribute_value("value")).is_equal_to(city_name)
            assert_that(self._tbl_forecast_list.is_element_displayed()).is_true()
            assert_that(actual_weather_data['txt_city_name'].get_text().lower()).contains(city_name)
            assert_that(actual_weather_data['txt_description'].get_text()).is_equal_to(expect_current_weather['weather'][0]['description'])
            assert_that(normalize("NFD", actual_weather_data['txt_weather_detail_content'].get_text())).is_equal_to(
                normalize("NFD", OpenWeatherResultData.TEMPERATURE_CONTENT.format(temp_main=expect_current_weather['main']['temp'],
                                                                 temp_min=expect_current_weather['main']['temp_min'], 
                                                                 temp_max=expect_current_weather['main']['temp_max'], 
                                                                 wind_speed=expect_current_weather['wind']['speed'],
                                                                 cloud_rate=expect_current_weather['clouds']['all'],
                                                                 hpa_value=expect_current_weather['main']['pressure']))
            )
            actual_lat_long = re.findall(r"[\d\.]+", actual_weather_data['txt_coordinate'].get_text())
            assert_that(round(float(actual_lat_long[0]), 2), expect_current_weather['coord']['lat'])
            assert_that(round(float(actual_lat_long[1]), 2), expect_current_weather['coord']['lon'])
            
    def verify_search_data_weather_result_is_not_found(self):
        assert_that(self._pnl_not_found.is_element_displayed()).is_true()
        actual_not_found_title = re.search(r"(?<=\n)[\w\s]+", self._pnl_not_found.get_text()).group(0)
        assert_that(actual_not_found_title, "Not found panel is not displayed").is_equal_to(OpenWeatherResultData.NOT_FOUND_PANEL)
