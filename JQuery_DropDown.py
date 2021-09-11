#its another method to select the dropdown
#its an costumize method
#dropdown select without an Select tag

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
        for l in range(len(value)):
            if ele.text == value[l]:
                ele.click() #it will click on given webelements
                break        #break the loop

#get the URL
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

#click on it
time.sleep(2)
driver.find_element(By.ID, 'justAnInputBox').click() #it will click on it an generate the drop down list


#get the dropdown list
time.sleep(2)
drop_down = driver.find_elements(By.XPATH, "//ul/li/span[@class='comboTreeItemTitle']")
value_list = ['choice 1', 'choice 2', 'choice 2 3']
select_option(drop_down, value_list) #call the define function


print("successfully run")

driver.close()
