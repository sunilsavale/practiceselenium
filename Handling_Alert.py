#handling alert pop up
#code by sunil savale
#dt- 02/09/2021

from selenium import webdriver



driver = webdriver.Chrome()
driver.maximize_window()

#get Url page
driver.get("http://demo.automationtesting.in/Alerts.html")


#handling of alert, click on alert wtih ok cancle
driver.find_element_by_xpath(".//a[@href='#CancelTab']").click()
driver.find_element_by_xpath(".//button[@onclick='confirmbox()']").click()


#store the alert in variable for reuse
alert = driver.switch_to.alert
#get the alert text
print(alert.text)
#switch to alert and cancle it
driver.switch_to.alert.dismiss()


#again generate alert pop up(click on alert with ok)
driver.find_element_by_xpath(".//a[@href='#OKTab']").click()
driver.find_element_by_xpath(".//button[@onclick='alertbox()']").click()


#i want to accept and get the alert text
alert2 = driver.switch_to.alert
print(alert2.text)
driver.switch_to.alert.accept()

print("Handling aletr pop up")
driver.close()