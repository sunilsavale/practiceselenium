#Assignment
#To get the list from the stack0verflow
#code by Sunil Savale
#Dt. 31/08/2021

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

#launch the browser
driver = webdriver.Chrome()


#get the StackOverflow Page
driver.get("https://insights.stackoverflow.com/survey/2021")
driver.maximize_window()


#Click on Technology
wait = WebDriverWait(driver,15)
Stake_over = wait.until(ec.presence_of_element_located((By.XPATH,".//li[@class='bt ds-bc py16']/a[contains(@href,'#technology')]"))).click()

#get the list of javascript and all language
language = wait.until(ec.visibility_of_element_located((By.XPATH,".//table[@id='language']/tbody/tr//td[position()]")))
list = driver.find_elements(By.XPATH,".//table[@id='language']/tbody/tr//td[position()]")


#All the language and there percentage will get
for x in list:
    y = x.text
    print(y)
driver.close()