from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.google.co.in")
driver.find_element_by_name("q").send_keys("Automation")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='FPdoLc VlcLAe']//input[@name='btnK']")))
ActionChains(driver).move_to_element(element).send_keys(Keys.ENTER).perform()
time.sleep(10)
print("Element Clickable")


# driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']").send_keys(Keys.ENTER)

print("Test Completed")
driver.close()
driver.quit()