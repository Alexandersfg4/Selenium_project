import pytest
import selenium.webdriver
from clients.data_client import DataClient

data_client = DataClient()
config = data_client.get_regular_data('config')


@pytest.fixture
def browser():
    
    # Initialize the WebDriver instance
    if config['browser'] == 'Safari':
        b = selenium.webdriver.Safari()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        b = selenium.webdriver.Chrome()          
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)    
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    b.implicitly_wait(config['implicit_wait'])
    
    # Return the WebDriver instance
    yield b
    
    # Quit the WebDriver instance for the cleanup
    b.quit()