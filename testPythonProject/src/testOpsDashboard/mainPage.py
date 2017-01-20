'''
Created on 19 Oca 2017

@author: nurd
'''

from testElements import BasePageElementMail
from testElements import BasePageElementPassword
from testLocators import MainPageLocatorsButton
from testLocators import MainPageLocatorsSuccessText


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        
    
class MailTextboxElement(BasePageElementMail):

    #The locator for search box where search string is entered
    locator = 'email'
    
class PasswordTextboxElement(BasePageElementPassword):

    #The locator for search box where search string is entered
    locator = 'password'
    
class MainPage(BasePage):

    #Declares a variable that will contain the retrieved text
    mail_textbox_element = MailTextboxElement()
    password_textbox_element = PasswordTextboxElement()


    def is_title_matches(self):
       
        return "AdTrust" in self.driver.title

    def click_submit_button(self):
        
        element = self.driver.find_element(*MainPageLocatorsButton.SUBMIT_BUTTON)
        element.click()
        
    def get_success_text(self):
        
        element = self.driver.find_element(*MainPageLocatorsSuccessText.SUCCESS_TEXT)
        return element.text
        