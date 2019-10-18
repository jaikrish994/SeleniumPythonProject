from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.get("https://www.google.co.in")
searchbox = driver.find_element_by_name("q")
searchbox.send_keys("raghav pal")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER).perform()
