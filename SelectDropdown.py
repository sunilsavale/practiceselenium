#select the all the dropdown from the dropdown values
#code by sunil savale
#date - 11/

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



def select_values(option_list, value):
    if not value[0] == 'all':
        for ele in option_list:
            print(ele.text)
            for l in range(len(value)):
                if ele.text == value[l]:
                    ele.click()
                    break
    else:
        try:
            for ele in option_list:
                ele.click()
        except Exception as e:
            print(e)

#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

#get the URL
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

#click on it
time.sleep(2)
driver.find_element(By.ID, 'justAnInputBox').click() #it will click on it an generate the drop down list


#get the dropdown list
time.sleep(2)
drop_down = driver.find_elements(By.XPATH, "//ul/li/span[@class='comboTreeItemTitle']")
value_list = ['all']
#value_list = ['choice 1', 'choice 2', 'choice 2 3']
#value_list = ['choice 2']
select_values(drop_down, value_list)
driver.close()