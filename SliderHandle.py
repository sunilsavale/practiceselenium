'''Handling the Slider'''


from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


class Slider():
    def SliderHandling(self):

        #Launch the Browser
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()

        #Navigate the URL
        driver.get("http://testautomationpractice.blogspot.com/")

        #slider works or not
        element = driver.find_element_by_xpath(".//span[contains(@class,'ui-slider-handle ')]")
        action = ActionChains(driver)
        '''Holds down the left mouse button on the source element,
           then moves to the target offset and releases the mouse button.'''
        #Multi way to handling the slider
        #way-1
        # action.drag_and_drop_by_offset(element, 70, 0).perform()
        #way-2
        # action.click_and_hold(element).pause(1).move_by_offset(80, 0).perform()
        #way-3
        action.move_to_element(element).pause(1).click_and_hold(element).move_by_offset(90, 0).release().perform()

        time.sleep(4)

Sliders = Slider()
Sliders.SliderHandling()
