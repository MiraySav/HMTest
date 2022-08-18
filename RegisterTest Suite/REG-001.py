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

# Join Here
menu = driver.find_element(By.XPATH, "//a[@class='menu__myhm'][normalize-space()='Sign in']")
action.move_to_element(menu).perform()
joinhere = driver.find_element(By.XPATH, "//a[normalize-space()='Not a Member yet? Join here!']")
action.move_to_element(joinhere).click().perform()
# Email
driver.find_element(By.XPATH, "//input[@id='modal-signin-email']").send_keys("miraytest123@gmail.com")
# Password
driver.find_element(By.XPATH, "//input[@id='modal-signin-password']").send_keys("Test123.")

# Date of Birth
driver.find_element(By.XPATH, "//input[@id='modal-signin-month']").send_keys("01")
driver.find_element(By.XPATH, "//input[@id='modal-signin-day']").send_keys("01")
driver.find_element(By.XPATH, "//input[@id='modal-signin-year']").send_keys("1997")
driver.find_element(By.XPATH, "//button[@class='button large js-submit-join']").click()
