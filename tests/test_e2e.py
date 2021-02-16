from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from tests.utilities.base_class import base_Class
from pageObjects.home_page import HomePage
from pageObjects.checkout import CheckOutPage
from pageObjects.confirmPage import ConfirmationPage


class TestOne(base_Class):
    def test_e2e(self):
        log = self.getLogger()
        # log.info or log.error, log.debug where we need in our code
        # here we create an obj for the PO class
        homeP_constr = HomePage(self.driver)
        checkP_const = homeP_constr.shopButton()
        # above we created an object for the check out page in the above method
        # - and we returne the object for the class as ckeckP_const
        # checkP_const = CheckOutPage(self.driver)
        items = checkP_const.getItems_name()
        i = -1
        for item in items:
            i = i + 1
            itemText = item.test
            if itemText == "Blackberry":
                checkP_const.add_toCard()[1].click()

        checkP_const.check_outCart.click()
        checkP_const.placeOrder_button.click()
        checkP_const.deliver_location.send_keys("ind")
        # Here we have the explicit wait in the base class and just optimizes here
        # chech base_Class
        self.verify_linkPresence("India")
        # Explicit wait
        #   wait = WebDriverWait(self.driver, 7)
        #  wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        checkP_const.checkBox_enable.click()
        confirm = checkP_const.purchase_Button
        # confirm = ConfirmationPage(self.driver)
        text = confirm.alert_Message.text

        assert "Success! Thank you!" in text
        self.driver.get_screenshot_as_file("screen.png")
