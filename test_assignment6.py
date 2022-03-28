# Worked with Matt Hannum
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver", chrome_options=options)

    def test_search_not_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("list comprehension")
        elem.send_keys(Keys.RETURN)
        self.assertIn("PEP 274", driver.page_source)


    def tearDown(self):
        self.driver.close()