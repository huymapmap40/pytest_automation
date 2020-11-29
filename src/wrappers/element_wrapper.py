from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.driver_constant import DriverConstant
from src.wrappers.browser_wrapper import BrowserWrapper
from typing import Tuple
from selenium import webdriver


class ElementWrapper:

    # locator argument input is equivalent with tuple (By.xx , value_of_by)
    def __init__(self, locator: Tuple[By, str]):
        self.__locator = locator

    # Method to get element by locator and it's value
    def __map(self) -> WebElement:
        try:
            return BrowserWrapper.instance_driver().find_element(self.__locator[0], self.__locator[1])
        except NoSuchElementException as E:
            print(E)
            print("Not found element by {} with value '{}'".format(self.__locator[0], self.__locator[1]))

    # Method return webdriver wait object
    def __wait(self):
        return WebDriverWait(BrowserWrapper.instance_driver(), DriverConstant.ELEMENT_TIMEOUT)

    def wait_clickable(self):
        self.__wait().until(EC.element_to_be_clickable(self.__locator))

    def wait_for_presence_of(self):
        self.__wait().until(EC.presence_of_element_located(self.__locator))

    def wait_for_visibility_of(self):
        self.__wait().until(EC.visibility_of_element_located(self.__locator))

    def click(self):
        self.wait_clickable()
        self.__map().click()

    def is_element_displayed(self):
        self.wait_for_visibility_of()
        try:
            return self.__map().is_displayed()
        except ElementNotVisibleException as E:
            print(E)

    def get_element_count(self):
        self.__map().find_elements(self.__locator[0], self.__locator[1]).count()

    def type(self, text):
        self.wait_for_visibility_of()
        try:
            return self.__map().send_keys(text)
        except ElementNotVisibleException as E:
            print(E)
            
    def press_key(self, key_value):
        self.wait_for_visibility_of()
        self.__map().send_keys(key_value)

    def get_text(self) -> str:
        self.wait_for_visibility_of()
        try:
            return self.__map().text
        except ElementNotVisibleException as E:
            print(E)

    def get_attribute_value(self, attribute_name):
        return self.__map().get_attribute(attribute_name)

    def move_mouse_and_click(self):
        action = ActionChains(BrowserWrapper.instance_driver())
        try:
            action.move_to_element(self.__map()).click().perform()
        except MoveTargetOutOfBoundsException as E:
            print(E)
