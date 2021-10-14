#Practice on Tricenties Site
#code by sunil Savale
#Date :- 14-10-2021


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class Id():
    def Generate_id(self):

        #Launch the browser
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()


        #navigate the url
        driver.get("http://obstaclecourse.tricentis.com/Obstacles/64161/retry")


        #click on Generate Button
        driver.find_element_by_id("generate").click()
        order_id = driver.find_element_by_xpath(".//div[contains(text(),'10')]")
        x = order_id.text
        print(x)


        #send keys to the input box
        driver.find_element_by_id("offerId").send_keys(x)
        print("click Id")
        time.sleep(5)

  
Generate = Id()
Generate.Generate_id()