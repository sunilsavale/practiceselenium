#MultiWindowHandle on Yatra.Com
#code by sunil savale
#date- 20-09-2021

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
import time


#Launch the Browser
class Windows():
    def MultiWindows(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()


        #Navigate the URL
        driver.get("https://www.yatra.com/")


        # get the parent window ids
        parent_window = driver.current_window_handle
        print(parent_window)
        time.sleep(5)


        # Click on Airline Web it will give us multiple airline
        window_handle = driver.find_element(By.XPATH, ".//img[contains(@src,'/2020/Jul/5b10fea20065899f659cec0ecee16bca.jpg')]").click()
        all_handles = driver.window_handles

        # get all the Window handles in the form of ids
        print(all_handles)

        #Switch to window and click on particular web element which is inspect
        for handle in all_handles:
            if handle != parent_window:
                driver.switch_to.window(handle)
                time.sleep(3)
                driver.find_element(By.XPATH, ".//a[@href='https://www.goair.in/plan-my-trip/web-check-in']").click()
                # wait = WebDriverWait(driver, 15)
                # input = wait.until(ec.visibility_of_element_located((By.XPATH, ".//input[@id='LastName']")))
                # input.click()
                # input.send_keys("Patil")
                driver.close()
                break
                #switch to parent window , back to the main window

        time.sleep(5)
        driver.switch_to.window(parent_window)
        driver.find_element(By.XPATH, ".//img[contains(@src,'/2020/Jul/5b10fea20065899f659cec0ecee16bca.jpg')]").click()


switch = Windows()
switch.MultiWindows()