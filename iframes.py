#practice on iframes
#code by sunil savale
#date :- 22-09-2021



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#launch the Browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


# naviagte the URL
driver.get("http://demo.automationtesting.in/Frames.html")
time.sleep(2)
driver.find_element_by_xpath("//a[@href='#Multiple']").click() #click on multiple


#searching a main iframe in page
iframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")

#swith to iframe
driver.switch_to.frame(iframe)

#wait to switch the iframe
time.sleep(3)
iframe2 = driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")


#swithching to iframe2
driver.switch_to.frame(iframe2)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Sunil") #keys send to input box
print("keys send or not")


time.sleep(2)
driver.quit()



