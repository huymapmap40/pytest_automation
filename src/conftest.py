import os
import pytest
import warnings
import urllib3
from datetime import datetime
from selenium import webdriver
from src.config.setup.driver_management import DriverManagement
from src.wrappers.browser_wrapper import BrowserWrapper


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Define browser to run")

@pytest.fixture(scope="class")
def setup_driver(request):
    browserName = request.config.getoption("--browser")
    config = DriverManagement.get_instance().init_driver(browser_name=browserName)
    BrowserWrapper.inject_driver(config.Driver)
    request.cls.driver = config.Driver
    yield
    config.Driver.quit()
