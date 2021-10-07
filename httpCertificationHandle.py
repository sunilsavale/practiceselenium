#handling the https certification or certification erron in selenium using by python
#is not an alert


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




'''Using the Optopn() we accept the certification erron and all'''

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
# Launch the browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

# Navigate the URL
driver.get("https://expired.badssl.com/")
print(driver.find_element_by_tag_name("h1").text)
driver.quit()