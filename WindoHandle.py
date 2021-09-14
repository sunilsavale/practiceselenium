#Window handling
#Get the Current window handle
#code by sunil savale
#date-14/09/2021


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#browser launching
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#navigate the URL
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/windows")

#get the current window handle
original_window = driver.current_window_handle
print(original_window)

#checking the length of window handle by using of assert
assert len(driver.window_handles) == 1

#click on it and it will open in window
driver.find_element_by_link_text('Click Here').click()

#wait for no.of window will be 2
wait.until(ec.number_of_windows_to_be(2))

#for loop  for the confirmation
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break


wait.until(ec.title_is("New Window"))
driver.quit()
