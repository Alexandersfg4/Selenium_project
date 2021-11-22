"""
This module contains HomePage,
the page object for the instagram's home page.
"""
from selenium.webdriver.common.by import By

class HomePage:
    
    BUTTON_BAR = (By.XPATH,  '/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li')
    SEARCH_BAR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input')
    ACCAUNT_BAR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div')
    
    def __init__(self, browser) -> None:
        self.browser = browser
        
    def get_buttons_bar(self):
        buttons = self.browser.find_elements(*self.BUTTON_BAR)
        return len(buttons)
    
    def get_account_bar(self):
        buttons = self.browser.find_elements(*self.ACCAUNT_BAR)
        return len(buttons)
        
    def get_search_bar(self):
        search_bar = self.browser.find_element(*self.SEARCH_BAR)
        return search_bar.text