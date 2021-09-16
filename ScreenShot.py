#Taking a screen shot on browser
#code by Sunil Savale


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
#launch the Browser
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()

#Naviagte the URL
driver.get("https://www.reddit.com/")
#driver.get_screenshot_as_file('reddit.png')


'''Full screenshor'''
#if you want to take screenshot of full web you need run browser in Hedaless mode
#use of lamda Expression

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_whole_page.png')