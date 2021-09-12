#move to Element by using ActionChains
#Code by Sunil Savale
#date- 12/09/2021



'''Practice on move to element'''


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
wait = WebDriverWait(driver, 10)

#get the URL
driver.get("https://www.spicejet.com/")

'''move to element perform by using actionchain classs'''
time.sleep(2)
login = wait.until(EC.presence_of_element_located((By.ID, "ctl00_HyperLinkLogin")))
#we create a ActionChains
action = ActionChains(driver)
action.move_to_element(login).perform()

#we also hover on spicemember
time.sleep(2)
member = wait.until(EC.presence_of_element_located((By.XPATH, ".//a[text()='SpiceClub Members']")))
action.move_to_element(member).perform()

time.sleep(2)
driver.close()
