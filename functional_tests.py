import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ExampleFunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_heading_text_is_correct(self):
        self.browser.get("http://localhost:8000")
        element: WebElement = self.browser.find_element(by=By.TAG_NAME, value="h1")
        self.assertEqual("Mental Health Tracker", element.text)

    def test_page_title_is_correct(self):
        self.browser.get("http://localhost:8000")
        
        self.assertEqual("PBD Mental Health Tracker", self.browser.title)
