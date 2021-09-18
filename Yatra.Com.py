#practice on yatra.Com

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#navigate the URL
driver.get("https://www.yatra.com/")
print(driver.title)

#Enter the Round trip details
driver.find_element_by_xpath(".//a[@title='Round Trip']").click() #click on Roun trip
from_to = driver.find_element_by_xpath(".//input[@id='BE_flight_origin_city']")
from_to.click()
# from_to.send_keys("Bangalore")
# from_to.send_keys(Keys.ENTER)
# time.sleep(5)

#Enter the Departure Details
time.sleep(3)
bangalore = driver.find_element(By.XPATH, ".//p[text()='Kempegowda International']/ancestor::li[position()<2]")
bangalore.click() #Enter the bangalore in departure location(Another way to select Bangalore Location is given above)


#Enter the Destination Details
driver.find_element_by_name("flight_destination").click()
time.sleep(5)
delhi = driver.find_element(By.XPATH, ".//p[text()='Indira Gandhi International']/ancestor::li[position()<2]")
delhi.click() #Enter the destination location

#Enter Departure Date
driver.find_element(By.XPATH, ".//input[contains(@name,'flight_origin_date')]/ancestor::label").click() #click on Date section for the choose the date
time.sleep(2)
all_dates = driver.find_elements(By.XPATH, ".//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

#select the dates using for loop
for date in all_dates:
    if date.get_attribute("data-date") == "22/09/2021":
        date.click()
        time.sleep(3)
        break
time.sleep(4)
return_ = driver.find_element(By.XPATH, ".//input[@id='BE_flight_arrival_date']")
retuen_date = all_dates = driver.find_elements(By.XPATH, ".//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
for x in retuen_date:
    if x.get_attribute("data-date") == "23/09/2021":
        x.click()
        time.sleep(5)
        break

#before the click on serach we need to add passenger details click on search and Close the browser
driver.find_element(By.XPATH, ".//span[contains(@class,'flight_passengerBox travellerPaxBox')]").click()
#click on Traveller
time.sleep(2)
Child = driver.find_element(By.XPATH, "(.//div//span[contains(@class,'ddSpinnerPlus')])[position()=1]")#add child by using doble click action chain
Child.click()
driver.find_element(By.XPATH, ".//div[@class='filter-list']").click()#CLick on Non Stop
driver.find_element(By.XPATH, ".//input[@type='submit']")#search for Flights

time.sleep(3)
driver.quit()