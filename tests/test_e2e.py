import time
from lib2to3.pgen2 import driver
from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from pageObjects.CourierServicePage import CourierServicePage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)
        homePage.interactiveService1().click()
        homePage.courierService1().click()
        courierService = CourierServicePage(self.driver)
        courierService.sendApplication1().click()
        courierService.clientName1().send_keys("Test Test")
        courierService.clientPhone1().send_keys("89245679078")
        courierService.clientText1().send_keys("Test text")
        courierService.buttonSubmit1().click()
        message = courierService.messageText1().text
        print(message)
        assert "Ваша заявка принята." in message
        courierService.inputValueOk1().click()







