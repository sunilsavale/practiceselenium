'''Practice on half ebay.com'''
'''code by sunil savale'''
'''date:- 13/10/2021'''


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# Launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)



# Navigate the url
driver.get("https://www.ebay.com/")
print(driver.title)


# search for the python and select the  books categpries
driver.find_element_by_id("gh-ac").send_keys("Python")
category = driver.find_element_by_id("gh-cat")
category.click()


#all categarious
allcaregories = driver.find_elements_by_xpath("(.//select[@class='gh-sb ']/option)[position() != 1]")
for ele in allcaregories:
    print(ele.text)
    if (ele.text) == "Books":
        ele.click()
        break


# Search the book
driver.find_element_by_id("gh-btn").click()


# click from all book to text book
textbook = driver.find_element_by_xpath(".//a[contains(@href,'https://www.ebay.com/sch/184644/i.html?')]")
textbook.click()



time.sleep(3)
driver.quit()