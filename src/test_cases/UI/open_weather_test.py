import pytest
from hamcrest import assert_that, equal_to
from src.data.general.page_urls import PageUrls
from src.wrappers.browser_wrapper import BrowserWrapper
from src.page_objects.open_weather.open_weather_home_page import OpenWeatherHomePage
from src.page_objects.open_weather.search_weather_result_page import SearchWeatherResultPage
from ..test_base import TestBase


class TestOpenWeather(TestBase):
        
        
    @pytest.mark.parametrize("city_name", ["ho chi minh", "ho chi minh, vn"])
    def test_search_weather_with_valid_city_and_display_results_correctly(self, city_name):
        TestOpenWeather().navigate_to(PageUrls.OPEN_WEATHER)
        open_weather_main_page = OpenWeatherHomePage.get_instance()
        search_result_page = open_weather_main_page.search_weather_in_your_city(city_name)
        search_result_page.verify_ui_result_page_is_displayed_correctly()
        search_result_page.verify_search_data_weather_result_is_correctly(city_name)
    
    
    @pytest.mark.xfail(reason="Bug-2")
    @pytest.mark.parametrize("invalid_city_name", ["hochiminh", "vn, ho chi minh", 
                                                   7000000000, "!@#$%^&*()", "vn"])
    def test_search_weather_invalid_city_and_display_not_found_result(self, invalid_city_name):
        TestOpenWeather().navigate_to(PageUrls.OPEN_WEATHER)
        open_weather_main_page = OpenWeatherHomePage.get_instance()
        open_weather_main_page.verify_open_weather_home_page_is_displayed()
        search_result_page = open_weather_main_page.search_weather_in_your_city(invalid_city_name)
        search_result_page.verify_ui_result_page_is_displayed_correctly()
        search_result_page.verify_search_data_weather_result_is_not_found()
    