from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


def Select_list(option_list, value):
    if not value[0] == 'all':
        for ele in option_list:
            print(ele.text)
            for l in range(len(value)):
                if ele.text == value[l]:
                    ele.click()
    else:
        try:
            for ele in option_list:
                ele.click()
        except Exception as g:
            print(g)


#get on the url
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)
driver.find_element(By.ID, "justAnInputBox1").click()

#multi option will generate
time.sleep(2)
multi_select = driver.find_elements_by_xpath(".//ul/li/span[@class='comboTreeItemTitle']")
value_list = ['choice 2', 'choice 1', 'choice 6']
#value_list = ['all']

#call the method
Select_list(multi_select, value_list)
#Select_list(multi_select, 'choice 2')

driver.close()