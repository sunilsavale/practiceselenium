'''Practice on double click and DragandDrop methods'''


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

#Launch the Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#Naviagte the Url
driver.get("http://testautomationpractice.blogspot.com/")


#double click on webelement on ui
double_click = driver.find_element_by_xpath(".//button[text()='Copy Text']")

'''ActionChains are a way to automate low level interactions such as
    mouse movements, mouse button actions, key press, and context menu interactions.
    This is useful for doing more complex actions like hover over and drag and drop.'''
action = ActionChains(driver)
action.double_click(double_click).perform()
print("Double click has sucessfully done")


#navigate the Url for Drag and Drop
driver.get("http://testautomationpractice.blogspot.com/")

#using ActionChains we will perform Drag and Drop
source = driver.find_element_by_id("draggable") #Draggable element
time.sleep(2)
target = driver.find_element_by_id("droppable") #droppable element


#use of new (ACtionChains) action class
action2 = ActionChains(driver)
action2.drag_and_drop(source, target).perform()


time.sleep(2)
driver.quit()