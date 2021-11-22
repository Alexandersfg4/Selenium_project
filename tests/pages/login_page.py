"""
This module contains LoginPage,
the page object for the instagram login page.
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    URL = "https://www.facebook.com/"
    lOGIN_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    ERROR_WINDOW = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div[1]/div[1]")
    
    def __init__(self, browser) -> None:
        self.browser = browser
        
    def load(self):
        self.browser.get(self.URL)
    
    def log_in(self, login, password):
        self.browser.find_element(*self.lOGIN_FIELD).send_keys(login)
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password + Keys.RETURN)
        # login_filed = self.browser.find_element(*self.lOGIN_FIELD)
        
    def window_unsuccessful_login(self):
        window = self.browser.find_element(*self.ERROR_WINDOW)
        return window.text
               