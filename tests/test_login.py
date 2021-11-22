import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import data_file
from time import sleep

def test_basic_login(browser):
    
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    
    # Open login page
    login_page.load()
    
    # Log in 
    login_page.log_in(data_file.login, data_file.password)
    sleep(5)
    home_page.get_buttons_bar()
    home_page.get_search_bar()
    home_page.get_account_bar()