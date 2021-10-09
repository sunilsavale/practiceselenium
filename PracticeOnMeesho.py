'''practice on the  meesho commercial site'''
'''What is difference between get() method and navigate method'''
'''get() is navigate the particular the URL and wait till page is load'''
'''driver.navigate() is navigate the particular the URL and does not wait until page is load and it maintains browser history and cookies to navigate back or forward '''
#Meesho site

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By



#launch the Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)


# Navigate the URL
driver.get("https://meesho.com/")


# mouse hover on women ethic and click on view all
target = driver.find_element_by_xpath(".//span[text()='Women Ethnic']")
action = ActionChains(driver)
action.move_to_element(target).perform()


#creating a explicit wait tonclick that element
wait = WebDriverWait(driver, 10)
ethic_wear = wait.until(ec.visibility_of_element_located((By.XPATH, ".//a[@href='/ethnicwear-women/pl/5v80d']/child::p")))
ethic_wear.click()


'''click on saree'''
saree = driver.find_element_by_xpath(".//div[contains(@class,'__DetailCard_Desktop-sc-j0e7tu-2 ewhMNY')]/ancestor::a[@href='/new-fashionable-sarees/p/wug2g']")
saree.click()


'''Add to Cart'''
addtocart = driver.find_element_by_css_selector("button[class='BaseButton-sc-1e0kf5s-0 hFIEMo']")
addtocart.click()


'''Get the title of the page'''
print(driver.title)


'''send the numbers to input box and click on send OTP if number is not correct it should show us message'''
driver.find_element_by_xpath(".//input[@type='tel']").send_keys("9898123211")
driver.find_element_by_xpath(".//span[text()='Send OTP']").click()

# quit the browser
driver.quit()