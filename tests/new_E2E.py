from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\WorkQA\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()
# "//div[@class = 'card h-100']/div/h4/a"
allProducs = driver.find_elements_by_xpath("//div[@class = 'card h-100']")

for product in allProducs:
    if product.find_element_by_xppath("div/h4/a").text == "Blackberry":
        product.find_element_by_css_selector(".btn.btn-info").click()

driver.find_element_by_xpath("//a[@class = 'nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class = 'btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")

# Explicit wait
wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_class_name("checkbox.checkbox-primary").click()
driver.find_element_by_css_selector("[type = 'submit']").click()
text = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in text
driver.get_screenshot_as_file("screen.png")
