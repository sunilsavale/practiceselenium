# Practice on Wolrd Population Counter
#Code by Sunil Savale
#date-15-09-2021

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#launch browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#Navigate the URL
driver.get("https://www.worldometers.info/world-population/")

#Capture Current World Population
world_population = driver.find_elements(By.XPATH, ".//div[@class='maincounter-number']/span[@class='rts-counter']")
todays_and_thisyear = driver.find_elements(By.XPATH, ".//div[text()='Today' or text()='This year']/parent::div//span[@class='rts-counter']")

#Create a While loop because of i want to break the and the get the data as required
n = 1
while n <= 20:
    print("--------current population-------")
    for ele in world_population:
        print(ele.text)
        print("--------Todays and This Year population-------")
        for ele1 in todays_and_thisyear:
            print(ele1.text)
            n = n+1
            if n == 20:
                break


driver.close()