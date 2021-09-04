from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

#launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

#get the URL
driver.get("http://demo.automationtesting.in/Register.html")

#on registration page and the information
driver.find_element_by_xpath(".//input[@placeholder='First Name']").click()
driver.find_element_by_xpath(".//input[@placeholder='First Name']").send_keys("name")
driver.find_element_by_xpath(".//input[@placeholder='Last Name']").click()
driver.find_element_by_xpath(".//input[@placeholder='Last Name']").send_keys("surname")
driver.find_element_by_xpath(".//div/textarea[@ng-model='Adress']").click()
driver.find_element_by_xpath(".//div/textarea[@ng-model='Adress']").send_keys("at:- Address ")

#radio button checking is enable or not, it will return us boolean if radio button enble or not
driver.find_element_by_xpath(".//label/input[@value='Male']").click()
male = driver.find_element_by_xpath(".//label/input[@value='Male']").is_enabled()
print(male)

#checking checkbox is selected or not , it will return us boolean value
driver.find_element_by_id("checkbox1").click()
cric = driver.find_element_by_id("checkbox1").get_attribute("value")
print(cric)

#its checking for checkbox select or not,it will return boolean value
cricket = driver.find_element_by_id("checkbox1").is_selected()
print(cricket)

#checking for language using of is_selected method
wait = WebDriverWait(driver, 15)
DD = wait.until(ec.presence_of_element_located((By.ID, "msdd")))
DD.click()
language = driver.find_elements_by_xpath("//ul[contains(@class,'ui-menu')]/li")
time.sleep(3)
language[1].click()
time.sleep(3)
language[23].click()
time.sleep(3)
language[40].click()
print(len(language))

for x in language:
    print(x.text)

driver.close()