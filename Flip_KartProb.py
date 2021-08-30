#Flipkart by automate scenario
#this is an interview Question related Programm
#Code by Sunil Savale
#Use of EXPLICIT_WAIT
##Dt.30/08/2021


from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
wait=WebDriverWait(driver,15)

#handling a alert using click method
driver.find_element_by_xpath(".//button[@class='_2KpZ6l _2doB4z']").click()


#click on electronic section and aslo use hover method
electronic=wait.until(ec.presence_of_element_located((By.XPATH,".//div[text()='Electronics']")))
ele = driver.find_element(By.XPATH,".//div[text()='Electronics']")
print(electronic.text)
webdriver.ActionChains(driver).move_to_element(ele).perform()


#click on laptop accessories
Laptop = wait.until(ec.visibility_of_element_located((By.XPATH,".//a[@class='_6WOcW9 _2-k99T']")))
driver.find_element(By.XPATH,".//a[@class='_6WOcW9 _2-k99T']").click()



#click on another electronics section
ele2=wait.until(ec.presence_of_element_located((By.XPATH,".//span[text()='Electronics']"))).click()


#find the apple section
apple = wait.until(ec.visibility_of_element_located((By.XPATH,".//a[@title='Apple']")))
driver.find_element(By.XPATH,".//a[@title='Apple']").click()



#shop of iphone XR and click on it
xr_iphone = wait.until(ec.presence_of_element_located((By.XPATH,".//a[contains(@href, '-xr-')]"))).get_attribute("href")
driver.find_element(By.XPATH,".//a[contains(@href, '-xr-')]").click()


#shop the i-phone in given list(3rd no. i-phone ) you should  click on it
shop=wait.until(ec.presence_of_element_located((By.XPATH,"(.//div[@class='col col-7-12']/div[@class='_4rR01T'])[3]")))
driver.find_element(By.XPATH,"(.//div[@class='col col-7-12']/div[@class='_4rR01T'])[3]").click()
print(shop.text)


print("Successfully shope by Automated")
driver.close()