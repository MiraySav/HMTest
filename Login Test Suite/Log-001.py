from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


serv_obj = Service("C:\WebDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://www2.hm.com/en_us/index.html")
driver.maximize_window()
driver.implicitly_wait(2)
action = ActionChains(driver)

# Accept Cookies
driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
# Login
driver.find_element(By.XPATH, "//a[@class='menu__myhm'][normalize-space()='Sign in']").click()
# Email
driver.find_element(By.XPATH, "//input[@id='modal-txt-signin-email']").send_keys("miraytest123@gmail.com")
# Password
driver.find_element(By.XPATH, "//input[@id='modal-txt-signin-password']").send_keys("Test123.")
driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Sign in']").click()