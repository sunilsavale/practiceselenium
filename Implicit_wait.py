#using implicit-wait programm will run

  #code by Sunil Savale
     #Date:-09 august 2021
from selenium import webdriver #import a package

driver=webdriver.Chrome()#Chrome driver
driver.get("http://demo.guru99.com/test/newtours")

print(driver.title) #get the tilte of the page
driver.implicitly_wait(10)#using a implicit wait ,waiting for action upto 10 sec

driver.find_element_by_xpath(".//input[@name='userName']").send_keys("mercury")#send keys in user name port

driver.find_element_by_xpath(".//input[@name='password']").send_keys("mercury")#send keys in user name port

driver.find_element_by_xpath(".//input[@name='submit']").click()#click on submit button

driver.close()#close the window after a completion of process

print("Usimg of implicit wait and close method")
