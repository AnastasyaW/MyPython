from selenium.webdriver.common.by import By
from pageObjects.confirmPage import ConfirmationPage


class CheckOutPage:
    # allProducs = self.driver.find_elements_by_xpath("//div[@class = 'card h-100']")
    # we create a constructor that will get the driver from
    # - the test case class and pass it here
    # we will also creat an ojbect of this class in the TC class:
    # homeP_constr = HomePage(self.driver)

    def __init__(self, driver):
        self.driver = driver

    all_items = (By.XPATH, "//div[@class = 'card h-100']")
    # item.find_element_by_css_selector(".btn.btn-info").click()
    addTo = (By.CSS_SELECTOR, ".btn.btn-info")
    check_out = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")
    # self.driver.find_element_by_xpath("//button[@class = 'btn btn-success']").click()
    # place order self.driver.find_element_by_xpath("//button[@class = 'btn btn-success']")

    place_order = (By.XPATH, "//button[@class = 'btn btn-success']")
    delivery_location = (By.ID, "country")
    # self.driver.find_element_by_class_name("checkbox.checkbox-primary").click()
    # self.driver.find_element_by_css_selector("[type = 'submit']").click()
    enable_checkBox = (By.CLASS_NAME, "checkbox.checkbox-primary")
    purchase_button = (By.CSS_SELECTOR, "[type = 'submit']")

    def purchase_Button(self):
        self.driver.find_element(CheckOutPage.purchase_button).click()
        confirm = ConfirmationPage(self.driver)
        return confirm

    def getItems_name(self):
        return self.driver.find_elements(*CheckOutPage.all_items)

    def add_toCard(self):
        return self.driver.find_element(*CheckOutPage.addTo)

    def check_outCart(self):
        return self.driver.find_element(CheckOutPage.check_out)

    def placeOrder_button(self):
        return self.driver.find_element(CheckOutPage.place_order)

    def deliver_location(self):
        return self.driver.find_element(CheckOutPage.delivery_location)

    def checkBox_enable(self):
        return self.driver.find_element(CheckOutPage.enable_checkBox)
