import requests
from src.apis.config.env_conf import OpenWeatherEnvironmentConfig as OpenWeather


class RequestHelper:
    
    HOST = OpenWeather.ENVIRONMENT_PARAMS[OpenWeather.ENVIRONMENT]['API_HOST']
    APPID = OpenWeather.ENVIRONMENT_PARAMS[OpenWeather.ENVIRONMENT]['API_KEY']
    appid_params = {'appid': APPID}
    request_headers = {'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                       'Accept-Encoding': 'gzip, deflate, br'}
    
    @staticmethod
    def send_get_request(endpoint, headers=None, params=''):
        request_headers = RequestHelper.request_headers
        if headers:
            request_headers.update(headers)
        params.update(RequestHelper.appid_params)
        return requests.get(RequestHelper.HOST + endpoint, params=params, headers=request_headers)
        
    @staticmethod
    def send_post_request(endpoint, headers=None, params='', data=''):
        request_headers = RequestHelper.request_headers
        if headers:
            request_headers.update(headers)
        params = RequestHelper.request_params.update(params)
        return requests.post(RequestHelper.HOST + endpoint, request_headers, params=params, data=data)
