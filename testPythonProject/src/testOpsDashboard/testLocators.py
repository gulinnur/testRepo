'''
Created on 19 Oca 2017

@author: nurd
'''

from selenium.webdriver.common.by import By

class MainPageLocatorsButton(object):
    
    SUBMIT_BUTTON = (By.ID, 'signin')
    
class MainPageLocatorsSuccessText(object):
    
    SUCCESS_TEXT = (By.CSS_SELECTOR, 'body > section > div > section > section > div > div > header > div > div > h2')
    
    

