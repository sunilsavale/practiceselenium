#right/context click practice
#code by sunil savale
#date-12/09/2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#get the URl
driver.get("https://www.jqueryscript.net/demo/Nested-Context-Menu-ggContextMenu/")

#find the Element
time.sleep(2)
right_click = driver.find_element_by_xpath(".//ul/li[@title='option 1']")

#create a ActionChain Class
action = ActionChains(driver)
action.context_click(right_click).perform()


#find out the values on right click
right_click_values = driver.find_elements_by_xpath("(.//div/ul)[3]")
for ele in right_click_values:
    print(ele.text)
    if ele.text == 'Option context 1':
        time.sleep(2)
        ele.click()
time.sleep(2)
#anothe context click on same page
driver.get("https://www.jqueryscript.net/demo/Nested-Context-Menu-ggContextMenu/")
right_click2 = driver.find_element(By.XPATH, ".//ul/li[@title='option 2']")
action = ActionChains(driver)
action.context_click(right_click2).perform()

time.sleep(4)
driver.quit()