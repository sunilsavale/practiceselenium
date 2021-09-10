from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

#Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

#use of WebDriverWait
wait = WebDriverWait(driver, 15)


#get the Url of oyo
driver.get("https://www.oyorooms.com/")

#click on mumbai
wait.until(ec.presence_of_element_located((By.XPATH, ".//a[@href='/hotels-in-mumbai/']")))
mumbai = driver.find_element_by_xpath(".//a[@href='/hotels-in-mumbai/']")
print(mumbai.text)
ActionChains(driver).move_to_element(mumbai).perform()
time.sleep(4)
all_mumbai = wait.until(ec.presence_of_element_located((By.XPATH, ".//div[text()='All of Mumbai']")))
all_mumbai.click()

#sort hotels by low to high price
DD = wait.until(ec.visibility_of_element_located((By.XPATH, ".//span[@class='dropdown__select']")))
DD.click()
low_to_high = wait.until(ec.presence_of_element_located((By.XPATH, ".//li/span[text()='Price Low to High']")))
low_to_high.click()



#in collection click on view more and click on nearby air-port
wait.until(ec.presence_of_element_located((By.XPATH, ".//span[text()='+ View More'][1]"))).click()
near_by = driver.find_element_by_xpath(".//div[text()='Near Airport']")
print(near_by.text)
near_by.click()
view_details = wait.until(ec.presence_of_element_located((By.XPATH, ".//div//button/span[text()='View Details'][1]")))
print(view_details.text)
view_details.click()



#click on guest policies
customer_policies = wait.until(ec.visibility_of_element_located((By.XPATH, ".//div[text()='View Guest Policy']")))
print(customer_policies.text)
customer_policies.click()


driver.close()









