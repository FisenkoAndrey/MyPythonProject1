from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest as pytest
from selenium import webdriver


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "*//span[text()='Интерактивные услуги']")
    interactiveService = (By.XPATH, "*//span[text()='Интерактивные услуги']")
    # self.driver.find_element(By.XPATH, "*//span[text()='Курьерская служба']").click()
    courierService = (By.XPATH, "*//span[text()='Курьерская служба']")

    def interactiveService1(self):
        return self.driver.find_element(*HomePage.interactiveService)

    def courierService1(self):
        return self.driver.find_element(*HomePage.courierService)