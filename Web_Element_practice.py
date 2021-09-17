#find Element from Element
#search for the child element
#from WebElement to child element
#code by Sunil Savale
#date-17/09/2021
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
search_form = driver.find_element(By.TAG_NAME, "form") #webelement
search_box = search_form.find_element(By.NAME, "q") #Child Element
search_box.send_keys("child element")

#Find Elements from Element
print("Find Elements from the Element")
#get the Url
driver.get("https://www.example.com/")

#Get the Element with the tag name
element = driver.find_element(By.TAG_NAME, "div")

#Get the all element with tag name 'p'
elements = element.find_elements(By.TAG_NAME, "p")
for e in elements:
    print(e.text)

#Get Active Element
print("Get the Active Element")
driver.get("http://www.google.com")
ele = driver.find_element_by_xpath(".//input[@name='q']")
ele.send_keys("webElement")


#Get the Attribute of current active widow(Get the Active Element)
attri = driver.switch_to.active_element.get_attribute("title")
print(attri)

driver.close()

