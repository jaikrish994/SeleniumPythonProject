from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, executable_path="../drivers/chromedriver.exe")
driver.get("https://www.google.co.in")
print(driver.title)
driver.close()
driver.quit()
print("Test Completed")