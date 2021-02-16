from selenium.webdriver.common.by import By


class ConfirmationPage:

    # text = self.driver.find_element_by_class_name("alert-success").text
    alert_message = (By.CLASS_NAME, "alert-success")


def aler_Message(self):
    return self.driver.find_element(ConfirmationPage.alert_message)