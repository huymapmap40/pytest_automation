## Download and install python
- Get [python 3](https://www.python.org/downloads/)
- Install python include "pip"

## IDE/Editor
__Window__:
 - [Pycharm](https://www.jetbrains.com/pycharm/)
 - [Vscode](https://code.visualstudio.com/)
 
 `Configure right python interpreter of system`

## Install dependencies
```
pip install -r requirements.txt
```

## Execute the UI test case example
### Config file
From *src/config/config_env_test.json*: setup to run with remote or local driver

### Run test case
 Stand at root path, use pytest commands with "--browser" option and specific test case:
  (*If not set --browser option, that default is chrome*)
- __Run specific test cases:__ `pytest src\test_cases\UI\<test_case_file>::<test_class_name>::<test_method_name> --browser=<browser_name>`
- __Run class test cases:__ `pytest src\test_cases\UI\<test_case_file>::<test_class_name> --browser=<browser_name>`
 
```
pytest src\test_cases\UI\open_weather_test.py::TestOpenWeather::test_search_weather_with_valid_city_and_display_results_correctly --browser=chrome
pytest src\test_cases\UI\open_weather_test.py::TestOpenWeather::test_search_weather_with_valid_city_and_display_results_correctly --browser=firefox
pytest src\test_cases\UI\open_weather_test.py::TestOpenWeather
```

## Run selenium grid with Docker compose:
*Install [docker](https://www.docker.com/)*

*Install [Vnc Viewer](https://www.realvnc.com/en/connect/download/viewer/)*

```
docker-compose up
```
- Set config (*config_env_test.json*) to run with remote webdriver
- Run example: `pytest src\test_cases\UI\open_weather_test.py::TestOpenWeather`

*__Use VncViewer to connect and view test run on containers:__*

- __Firefox node__: `localhost:32772`
- __Chrome node__: `localhost:32771`

  Password: `secret`

## Run multiple browser
- Config running test cases from *config/parallel_test*
- Excute python *run_paralel_test.py* : `python <working_path>/run_parallel_test.py`
- Logs file for each tests will be written in *reports/concurrent_test_logs*

## View Test report
- Uncomment lines in __pytest.ini__ to enable test report
- Html report will be store in *reports/html*


