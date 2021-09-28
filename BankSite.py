from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


#Launch the browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#navigathe URL
driver.get("https://parabank.parasoft.com/")

#click on admin portal
driver.find_element_by_xpath(".//a[text()='Admin Page']").click()


'''Data'''
#click on initialized
driver.find_element_by_xpath(".//table[@class='form2']//tbody/tr/td/button[@value='INIT']").click()

#choose of Data Access Mode
driver.find_element_by_id("accessMode1").click()

#click on WSDL
print(len(driver.current_window_handle))
driver.find_element_by_xpath(".//a[starts-with(@href,'services/ParaBank?wsdl')]").click()
windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    print(driver.title)

time.sleep(2)

#driver back
#driver.back()
driver.close()