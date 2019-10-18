import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class MyTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_search1(self):
        self.driver.get("https://www.google.co.in")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']").send_keys(Keys.ENTER)
        x = self.driver.title
        print(x)
        self.assertEqual(x,"Automation step by step - Google Search")
    def test_search2(self):
        self.driver.get("https://www.google.co.in")
        self.driver.find_element_by_name("q").send_keys("raghav pal")
        self.driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']").send_keys(Keys.ENTER)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "raghav pal - Google Search")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()

#     def test_something(self):
#         self.assertEqual(True, False)
#
#
if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/computer/PycharmProjects/Selenium/reports'), verbosity=2)
    unittest.main(verbosity=2)

