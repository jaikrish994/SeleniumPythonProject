import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.google.co.in")
time.sleep(3)
driver.maximize_window()
text = driver.find_element_by_name('q').send_keys("Automation Step by Step")
time.sleep(3)
ActionChains(driver).send_keys(Keys.ENTER).perform()
link = driver.find_element_by_xpath("//h3[contains(text(),'YouTube')]")
ActionChains(driver).click(link).send_keys(Keys.CONTROL+'t').perform()




