from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from tests.utilities.base_class import base_Class
from pageObjects.checkout import CheckOutPage


class HomePage:
    # We declare a constructor here that will receive the driver
    # - from the test case class
    # and we also have to create an object of this class into
    # - the test case class: homeP_constr = HomePage(self.driver)
    def __init__(self, driver):
        self.driver = driver

    # now this is the step we need to create:
    # self.driver.find_element_by_link_text("Shop").click()
    #
    shopIcon = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name ='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    genders = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type = 'submit']")
    sucMessage = (By.CLASS_NAME, "alert-success ")

    def suc_Msg(self):
        return self.driver.find_element(HomePage.sucMessage)

    def submit_Button(self):
        return self.driver.find_element(HomePage.submit)

    def shopButton(self):
        self.driver.find_element(*HomePage.shopButton).click()
        checkP_const = CheckOutPage(self.driver)
        return checkP_const

    def enter_Name(self):
        return self.driver.find_element(HomePage.name)

    def enter_Email(self):
        return self.driver.find_element(HomePage.email)

    def enter_Pass(self):
        return self.driver.find_element(HomePage.password)

    def check_Box(self):
        return self.driver.find_element(HomePage.checkBox)

    def pick_Genger(self):
        return self.driver.find_element(HomePage.genders)
