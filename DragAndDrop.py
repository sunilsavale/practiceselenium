#practice on DragAndDrop method
#Code by Sunil Savale
#Date- 12/09/2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#define the function
def DragAndDrop():
    action = ActionChains(driver)
    '''there are two way to DragAndDrop  '''
    #action.drag_and_drop(source, target).perform()
    #anoter way to draganddrop given below
    time.sleep(2)
    action.click_and_hold(source4).move_to_element(target).release().perform()
    print(driver.title)

#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#get on the particular site
driver.get("https://www.jqueryscript.net/demo/Mobile-Drag-Drop-Plugin-jQuery/")

#find the wenelements
source = driver.find_element(By.XPATH, ".//button[text()='Drag me']")
source2 = driver.find_element(By.XPATH, ".//button[@class='btn btn-primary draghandle draggable dragaware']")
source3 = driver.find_element(By.XPATH, ".//button[text()='Drag and Drop me']")
source4 = driver.find_element(By.XPATH, "(.//span[@class='draggables draggable dragaware']/button)[1]")
target = driver.find_element(By.XPATH, ".//div/p[text()='Drop here']")


#call the define function
DragAndDrop()
time.sleep(2)
driver.quit()
