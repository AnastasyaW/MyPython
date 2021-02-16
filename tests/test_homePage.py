from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pageObjects.home_page import HomePage
import pytest
from TestData.homePageData import HomePageData


class TestHomePage(base_Class):
    def test_formSubmit(self, get_screenshot_as_file):
        homePage = HomePage(self.driver)
        homePage.enter_Name().send_keys(getData["firstName"])
        homePage.enter_Email().send_keys(getData["email"])
        homePage.enter_Pass().send_keys(getData["password"])
        homePage.check_Box().click()

        self.selectOptionBytext(homePage.pick_Genger(), getData["gender"])
        homePage.submit_Button.click()

        success = homePage.suc_Msg.text
        print(success)
        assert "Success" in success
        print("_____________ _____________________________________")
        # to run the 2 sets of data, and if the driver won't navigate
        # - to a new page, then we will need to refresh the page
        # - ex:
        self.driver.refresh()


@pytest.fixture(params=HomePageData.getTestDataExcell("Testcase2"))
def getData(self, request):
    return request.params
