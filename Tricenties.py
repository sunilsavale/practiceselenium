#Practice on Tricenties Site
#code by sunil Savale
#Date :- 25-09-2021


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


#Launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


#Navigate the URL
driver.get("https://obstaclecourse.tricentis.com/Obstacles/22505/retry#")


#click on
time.sleep(2)
driver.find_element_by_id("dontuseid").click()


#Navigate the Another URL
driver.get("https://obstaclecourse.tricentis.com/Obstacles/14090?retry=1")


#click on Generate Button
driver.find_element_by_id("generate").click()


#click on Seelct Drop Down starring with 'M'
driver.find_element_by_xpath("(.//select[@class='tableselect value'])[position()=1]").click()
drop_down = driver.find_elements_by_xpath(".//td[text()='Select word that starts with letter: M']/parent::tr/child::td[@class='value']/select/option")


#click on one of drop down
for x in drop_down:
    print(x.text)
    if (x.text) == "Mobile":
        time.sleep(3)
        x.click()


#click on Select DropDown starting with 'S'
driver.find_element_by_xpath("(.//select[@class='tableselect value'])[position()=4]").click()
dro_down = driver.find_elements_by_xpath(".//td[text()='Select word that starts with letter: S']/parent::tr/child::td[@class='value']/select/option")
for s in dro_down:
    if (s.text) == "SmartID":
        s.click()


#click on Select DropDown starting with 'E'
driver.find_element_by_xpath("(.//select[@class='tableselect value'])[position()=2]").click()
dro_dow = driver.find_elements_by_xpath(".//td[text()='Select word that starts with letter: E']/parent::tr/child::td[@class='value']/select/option")
for E in dro_dow:
    if (E.text) == "SmartID":
        E.click()

driver.quit()