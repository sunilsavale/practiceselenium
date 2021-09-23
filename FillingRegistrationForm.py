
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time


class RegistrationForm():
    def Information(self):
        #lauch the Browser
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window() #maximize the window

        #Navigate the URL
        driver.get("http://demo.automationtesting.in/Register.html")

        #Enter the first Name and Last name
        driver.find_element_by_xpath(".//input[@placeholder='First Name']").send_keys("Sunil")
        driver.find_element_by_xpath(".//input[@placeholder='Last Name']").send_keys("Patil")

        #Enter the address
        driver.find_element_by_tag_name("textarea").send_keys("At:- Dhule, Dist:- Dhule")
        driver.find_element_by_xpath(".//input[@type='email']").send_keys("sunilpatil@gmail.com")
        driver.find_element_by_xpath(".//input[@type='tel']").send_keys("9898989898")

        #Select the gender and hobbies

        driver.find_element_by_xpath(".//input[@value = 'Male']").click()
        driver.find_element_by_id("checkbox1").click()
        driver.find_element_by_id("checkbox2").click()
        driver.find_element_by_id("checkbox3").click()
        time.sleep(4)

        #select the language
        driver.find_element_by_id("msdd").click()
        time.sleep(3)
        langauge = driver.find_elements_by_xpath(".//ul[contains(@class,'ui-aut')]/li/a")
        print(len(langauge))
        for list in langauge:
            print(list.text)
            time.sleep(1)
            if list.text == "Arabic":
                list.click()
            if list.text == "Croatian":
                list.click()
            if list.text == "English":
                list.click()
            if list.text == "Hindi":
                list.click()
                break #Break the loop when the text is

        #select the skill and country and all
        driver.find_element_by_id("Skills").click()
        skill = driver.find_elements_by_xpath(".//select[@id='Skills']/option")
        print(len(skill))
        for skills in skill:
            if skills.get_attribute("value") == "Adobe Photoshop":
                skills.click()
            if skills.get_attribute("value") == "APIs":
                skills.click()

        #Country selection
        driver.find_element_by_xpath(".//span[@class='select2-selection select2-selection--single']").click()
        country = driver.find_elements_by_xpath(".//ul[@id='select2-country-results']/li")
        print(len(country))
        for countries in country:
            print(countries.text)
            if countries.text == "Hong Kong":
                countries.click()


info = RegistrationForm()
info.Information()
