#How to run browser in Headless Mode


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#creat the headless mode and launch the broser as in Headless mode
option = webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

#Navigate the URL 
driver.get("https://www.snapdeal.com/")

#get the title of the page
print(driver.title)
driver.quit()
