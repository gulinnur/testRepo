import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OperationalDashboardLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()


    def test_login_ops_fail(self):
        user = "nur.demirparmak@comodo.com"
        pwd = "123456"
        driver = self.driver
        driver.get("http://operations.staging.adtrustmedia.com/login")
        assert "AdTrustMedia" in driver.title
        driver.implicitly_wait(10)
        elem = driver.find_element_by_id("email")
        elem.send_keys(user)
        elem = driver.find_element_by_id("password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
       
        elem = driver.find_element_by_css_selector("body > section > div > div > div.panel-body > div > p")
        message = elem.text
        self.assertEqual(message, "Incorrect username or password.")
    
    def test_login_ops_pass(self):
        user = "mustafa.oger@comodo.com"
        pwd = "123456"
        driver = self.driver
        driver.get("http://operations.staging.adtrustmedia.com/login")
        assert "AdTrustMedia" in driver.title
        driver.implicitly_wait(10)
        elem = driver.find_element_by_id("email")
        elem.send_keys(user)
        elem = driver.find_element_by_id("password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
       
        elem = driver.find_element_by_css_selector("body > section > div > section > section > div > div > header > div > div > h2")
        message = elem.text
        self.assertIn("Welcome Mustafa", message)
       
       
    def test_add_new_role(self):
        user = "mustafa.oger@comodo.com"
        pwd = "123456"
        driver = self.driver
        driver.get("http://operations.staging.adtrustmedia.com/login")
        driver.implicitly_wait(10)
        elem = driver.find_element_by_id("email")
        elem.send_keys(user)
        elem = driver.find_element_by_id("password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
       
        driver.implicitly_wait(100)
        role_name = "Gulin Test"
        driver.find_element_by_id("settings").click()
        driver.find_element_by_id("role-menu").click()
        driver.find_element_by_id("createRoleBtn").click()
        elem = driver.find_element_by_id("role")
        elem.send_keys(role_name)
        driver.find_element_by_id("create").click()
       
        elem = driver.find_element_by_css_selector(".ui-pnotify-text")
        message = elem.text
        self.assertIn("Role name added", message)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()