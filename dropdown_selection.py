#Drop Down selection
#code by sunil savale
#Date 12/09/2021

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# get the URL
driver.get("http://demo.automationtesting.in/Register.html")

# on registration page and the information
driver.find_element_by_xpath(".//input[@placeholder='First Name']").click()
driver.find_element_by_xpath(".//input[@placeholder='First Name']").send_keys("name")
driver.find_element_by_xpath(".//input[@placeholder='Last Name']").click()
driver.find_element_by_xpath(".//input[@placeholder='Last Name']").send_keys("surname")
driver.find_element_by_xpath(".//div/input[@type='email']").send_keys("xyz@gmail.com")
driver.find_element_by_xpath(".//div/input[@type='tel']").send_keys("8877722932")
driver.find_element_by_xpath(".//div/textarea[@ng-model='Adress']").click()
driver.find_element_by_xpath(".//div/textarea[@ng-model='Adress']").send_keys("at:- Address ")

# radio button checking is enable or not, it will return us boolean if radio button enble or not
driver.find_element_by_xpath(".//label/input[@value='Male']").click()
male = driver.find_element_by_xpath(".//label/input[@value='Male']").is_enabled()
print(male)

# checking checkbox is selected or not , it will return us boolean value
driver.find_element_by_id("checkbox1").click()
cric = driver.find_element_by_id("checkbox1").get_attribute("value")
print(cric)

# its checking for checkbox select or not,it will return boolean value
cricket = driver.find_element_by_id("checkbox1").is_selected()
print(cricket)

# checking for language using of def method select the multiple option from the list
wait = WebDriverWait(driver, 15)
DD = wait.until(ec.visibility_of_element_located((By.ID, "msdd")))
DD.click()


def SelectionLanguage(*args):
    language = driver.find_elements_by_xpath(".//ul[contains(@class,'ui-menu')]/li")
    if len(language) > 0:
        time.sleep(2)
        language[args[0]].click()
        time.sleep(2)
        language[args[1]].click()
        time.sleep(2)
        language[args[2]].click()
SelectionLanguage(1,5,6)


#select the skill from the dropdown skill
skill = driver.find_element_by_xpath(".//div/select[@id='Skills']")
select = Select(skill)
time.sleep(2)
select.select_by_index(1)
time.sleep(2)
select.select_by_value("Python")


#countries selection and how many countries there
total_contries = driver.find_elements_by_xpath(".//div//select[@id='countries']/option")
print(len(total_contries))
countries = driver.find_element_by_xpath(".//div//select[@id='countries']")
countries_selection = Select(countries)
countries_selection.select_by_value("India")


#Enter the date of birth
#enter the year
year = driver.find_element_by_id("yearbox")
year_select = Select(year)
year_select.select_by_value("1993")
#enter the month
month = driver.find_element_by_xpath("//div/select[@ng-model='monthbox']")
month_select = Select(month)
month_select.select_by_value("August")
#enter the date
date = driver.find_element_by_id("daybox")
date_select = Select(date)
date_select.select_by_value("17")


#creating a password
#enter the password
password = driver.find_element_by_xpath(".//div/input[@id='firstpassword']")
password.click()
password.send_keys("123455")
#confirmation of password
password_confirmatiion = driver.find_element_by_xpath(".//div/input[@id='secondpassword']")
password_confirmatiion.click()
password_confirmatiion.send_keys("123455")


#upload the image
image = driver.find_element_by_xpath(".//div/input[@id='imagesrc']")
image.send_keys(r"C:\Users\sunil\Downloads\4153841.jpg")


#click on submit button
submit = driver.find_element_by_id("submitbtn").click()



driver.close()




