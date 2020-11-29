import urllib
from .request_helper import RequestHelper
from . import constant


class CurrentWeatherHelper:
    
    @staticmethod
    def get_current_weather_by_city(city_name, units='metric'):
        params = {
            # 'q': urllib.parse.quote(city_name),
            'q': city_name,
            'units': units
        }
        return RequestHelper.send_get_request(constant.CURRENT_WEATHER, params=params)
