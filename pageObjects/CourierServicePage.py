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


class CourierServicePage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "*//a[text()='Подать заявку']").click()
    sendApplication = (By.XPATH, "//a[text()='Подать заявку']")

    # self.driver.find_element(By.CSS_SELECTOR, "#OrderTxtClientName").send_keys("Test Test")
    clientName = (By.CSS_SELECTOR, "#OrderTxtClientName")

    # self.driver.find_element(By.CSS_SELECTOR, "#OrderTxtClientPhone").send_keys("89245679078")
    clientPhone = (By.CSS_SELECTOR, "#OrderTxtClientPhone")

    # self.driver.find_element(By.CSS_SELECTOR, "#OrderTxtClientOrder").send_keys("Test text")
    clientText = (By.CSS_SELECTOR, "#OrderTxtClientOrder")

    # self.driver.find_element(By.CSS_SELECTOR, "#OrderBtnSubmit").click()
    buttonSubmit = (By.CSS_SELECTOR, "#OrderBtnSubmit")

    # self.driver.find_element(By.CSS_SELECTOR, "input[value='OK']").click()
    inputValueOk = (By.CSS_SELECTOR, "input[value='OK']")

    # self.driver.find_element(By.XPATH, "*//span[@id='IndexDivMessageText']//b").text
    messageText = (By.XPATH, "*//span[@id='IndexDivMessageText']//b")

    def sendApplication1(self):
        return self.driver.find_element(*CourierServicePage.sendApplication)

    def clientName1(self):
        return self.driver.find_element(*CourierServicePage.clientName)

    def clientPhone1(self):
        return self.driver.find_element(*CourierServicePage.clientPhone)

    def clientText1(self):
        return self.driver.find_element(*CourierServicePage.clientText)

    def buttonSubmit1(self):
        return self.driver.find_element(*CourierServicePage.buttonSubmit)

    def inputValueOk1(self):
        return self.driver.find_element(*CourierServicePage.inputValueOk)

    def messageText1(self):
        return self.driver.find_element(*CourierServicePage.messageText)