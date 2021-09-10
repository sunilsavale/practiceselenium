#select method use only where drop down is implemented using Select tag
#code by sunil savale
#dt 10/09/2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#get the the URL
driver.get("https://www.orangehrm.com/hris-hr-software-demo")
print(driver.title)


#enter a name
driver.find_element_by_xpath(".//input[@name='FirstName']").send_keys("sunil")
driver.find_element_by_xpath(".//input[@name='LastName']").send_keys("patil")
driver.find_element_by_xpath(".//input[@name='Email']").send_keys("sunny@gmail.com")
driver.find_element_by_xpath(".//input[@name='Contact']").send_keys("3834329244")


#DropDown Custumize method
def DropDownSelection(DD_list, value):
    print(len(DD_list))
    for ele in DD_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
#driver.find_element_by_name("Country").click()
country_option = driver.find_elements(By.XPATH, ".//div/select[@id='Form_submitForm_Country']/option")
DropDownSelection(country_option, 'India')


#Use of Select method to select DropDown
driver.get("https://www.orangehrm.com/hris-hr-software-demo")
country_option = driver.find_element(By.XPATH, ".//div/select[@id='Form_submitForm_Country']")
select = Select(country_option)
select.select_by_visible_text('India')


#another method the select dropdown
driver.get("https://www.orangehrm.com/hris-hr-software-demo")
def Select_dropdown(element, value):
    selct = Select(element)
    selct.select_by_value(value)
country_list = driver.find_element(By.XPATH, ".//div/select[@id='Form_submitForm_Country']")
Select_dropdown(country_list, 'India')


driver.close()
