import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.google.co.in")
        cls.driver.maximize_window()
    def test_search_automation(self):
        self.driver.get("https://www.google.co.in")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']").send_keys(Keys.ENTER)
        print(self.driver.title)
    def test_search_raghav(self):
        self.driver.get("https://www.google.co.in")
        self.driver.find_element_by_name("q").send_keys("raghav pal")
        # self.driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("btnk1").send_keys(Keys.ENTER)
        print(self.driver.title)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

#
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/computer/PycharmProjects/Selenium/reportss"))
