#Using the Javascript to perform click action on web element
#When normal method of click not work instead of that you can used javascript click

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# launch the Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#Navigate the URL
driver.get("https://www.flipkart.com/")

#handling the Loging Pop up
login = driver.find_element(By.XPATH, ".//button[@class='_2KpZ6l _2doB4z']")
driver.execute_script("arguments[0].click();", login)

# get the title the page by using Java script
print(driver.execute_script('return document.title'))

# Using Javascipt Click will perform
time.sleep(5)
top_offer = driver.find_element(By.XPATH, "(.//div[text()='Top Offers'])[position()=1]")


#use of java script to perform click action
driver.execute_script("arguments[0].click();", top_offer)


#Scrilling down the page using java script
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #Scroll down the page 


time.sleep(3)
driver.quit()
