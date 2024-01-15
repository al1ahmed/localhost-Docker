import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDevopsProject(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get(r'Z:\nu\devops\beginner-html-site-styled-gh-pages\index.html')

    def test_group_members(self):
        welcome_message = self.driver.find_element(By.TAG_NAME,"h1")
        assert welcome_message.text == "Mozilla is cool"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()