
class OpenWeatherResultData:
    
    HEADER_TITLE = "Weather in your city"
    TEMPERATURE_CONTENT = "{temp_main}°С temperature from {temp_min} to {temp_max} °С, wind {wind_speed} m/s. clouds {cloud_rate} %, {hpa_value} hpa"
    GUIDELINE_TITLE = "Search engine is very flexible. How it works:"
    GUIDELINE_CONTENT = "To make it more precise put the city's name, comma, 2-letter country code (ISO3166). You will get all proper cities in chosen country.\nThe order is important - the first is city name then comma then country. Example - London, GB or New York, US."
    NOT_FOUND_PANEL = "Not found"
