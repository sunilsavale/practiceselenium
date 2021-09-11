#JQuery Multi Dropdown selection
#code by Sunil Savale
#date- 11/09/2021


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#Creating a method to click on Webelement
def select_option(option_list, value):
    for ele in option_list:
        print(ele.text)
        if ele.text == value:
           ele.click()   #it will click on given webelements

#get the URL
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

#click on it
time.sleep(2)
driver.find_element(By.ID, 'justAnInputBox').click() #it will click on it an generate the drop down list


#get the dropdown list
time.sleep(2)
drop_down = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
select_option(drop_down, 'choice 1') #call the define function
select_option(drop_down, 'choice 2 2')
select_option(drop_down, 'choice 4')

print("successfully run")

driver.close()
