import os


class OpenWeatherEnvironmentConfig:
    ENVIRONMENT = os.getenv('ENV', 'TEST')
    ENVIRONMENT_PARAMS = {
        'TEST': {
            'API_HOST': 'http://api.openweathermap.org/data/2.5',
            'API_KEY': '6ed6705c4bff2b9e5844ccae25eaa563'
        }
    }
