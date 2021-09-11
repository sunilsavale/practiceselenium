
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/Echo-Dot-3rd-Gen/dp/B07PFFMP9P")

wait = WebDriverWait(driver,10)

Main_Window=driver.current_window_handle
    
assert len(driver.window_handles)==1 #it will check no. of window on browser
    
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-share-facebook']").click()

Wait_for=wait.until(ec.number_of_windows_to_be(2)) #it will check no. of. window

for x in driver.window_handles:
    if x != Main_Window:
        driver.switch_to.window(x)
        break
print("done")
print(driver.title)
print("Facebook:- Fb url is below")
print(driver.current_url)

driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']").send_keys("Amazon")
list_of_amazon=driver.find_elements(By.CSS_SELECTOR,"ul.erkvQe li span")
print(len(list_of_amazon))

for x in list_of_amazon:
    print(x.text)
print(driver.title)

