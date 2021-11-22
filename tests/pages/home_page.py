"""
This module contains HomePage,
the page object for the instagram's home page.
"""
from selenium.webdriver.common.by import By

class HomePage:
    
    BUTTON_BAR = (By.XPATH,  '/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li')
    SEARCH_BAR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input')
    ACCOUNT_BAR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div')
    
    def __init__(self, browser) -> None:
        self.browser = browser
        
    def check_buttons_bar(self):
        buttons = self.browser.find_elements(*self.BUTTON_BAR)
        assert len(buttons) == 6, "Elements on the button bar is not enough"
    
    def check_account_bar(self):
        buttons = self.browser.find_elements(*self.ACCOUNT_BAR)
        assert len(buttons) == 4, "Elements on the account bar is not enough"
        
    def check_search_bar(self):
        search_bar = self.browser.find_element(*self.SEARCH_BAR)
        assert search_bar.get_attribute('aria-label') == "Поиск на Facebook"