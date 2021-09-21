from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

#Launch the Browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#Navigate the URL
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')
search.send_keys("wikipedia.com")
search.send_keys(Keys.ENTER)

#click on Wikipedia
driver.find_element_by_xpath(".//h3[text()='Wikipedia']").click() #click on wikipedia

#search for Giga berlin
giga_berlin = driver.find_element_by_id("searchInput")
giga_berlin.click()
giga_berlin.send_keys("Giga Berlin")
driver.find_element_by_xpath(".//button[@class='pure-button pure-button-primary-progressive']").click()

#get the Co-ordinates
cordinates = driver.find_element_by_xpath("(.//span[contains(@class,'geo-dec')])[position()=1]")
print(driver.title)
print(cordinates.text)
cordinates.click()

#click on google map
google_map = driver.find_element_by_xpath("(.//a[contains(@href,'//www.google.com/maps')])[position()=1]")
google_map.get_attribute("href")
google_map.click()
print(driver.title)

time.sleep(4)
driver.quit()