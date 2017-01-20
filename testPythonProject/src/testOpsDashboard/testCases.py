'''
Created on 19 Oca 2017

@author: nurd
'''
import unittest
from selenium import webdriver
import mainPage


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://operations.staging.adtrustmedia.com/login")


    def tearDown(self):
        self.driver.close()


    def testSuccessfullyLogin(self):
        main_page = mainPage.MainPage(self.driver)
        
        assert main_page.is_title_matches(), "title doesn't match."
        main_page.mail_textbox_element = "mustafa.oger@comodo.com"
        main_page.password_textbox_element = "123456"
        main_page.click_submit_button()
        
        self.assertIn("Welcome Mustafa", main_page.get_success_text())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()