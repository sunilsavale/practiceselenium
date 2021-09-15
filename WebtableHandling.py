#handling the web talble
#code by sunil savale
#date - 15/09/2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time


#launch the Browser
driver = webdriver.Chrome(ChromeDriverManager().install())

#navigate the URL
driver.get('https://courses.letskodeit.com/practice')

#inspectng the webtable
table = driver.find_elements_by_xpath(".//table[@id='product']/tbody/tr[position()]")
table1 = driver.find_elements_by_xpath(".//table[@id='product']/tbody/tr[position()>2]")

select = driver.find_elements_by_id("multiple-select-example")
action = ActionChains(driver)

mytabel= []
#for the get table we need to use for loop
for ele in table:
    print(ele.text)
    mytabel.append(ele.text)
print('*'*50)
for ele2 in table1:
    print(ele2.text)
print('*'*50)
for x in select:
    print(x.text)

#click on apple web element by using action class
target = driver.find_element_by_xpath(".//option[text()='Apple']")
action.click(target).perform()
time.sleep(4)


driver.quit()