import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from clients.data_client import DataClient
from time import sleep

data_client = DataClient()
credentials = data_client.get_regular_data('valid_user_data')

def test_basic_login(browser):
    
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    
    # Open login page
    login_page.load()
    
    # Log in 
    login_page.log_in(credentials['login'], credentials['password'])
    
    home_page.check_buttons_bar()
    home_page.check_search_bar()
    home_page.check_account_bar()
    
def test_login_invalid_data(browser):
    
    login_page = LoginPage(browser)
    
    # Open login page
    login_page.load()
    
    # Log in 
    login_page.log_in(credentials['login'], 'password')
  
    # Check that error window is presented
    login_page.window_unsuccessful_login()