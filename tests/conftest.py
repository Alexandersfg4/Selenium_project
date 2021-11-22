import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    
    # Initialize the Safari instance
    b = selenium.webdriver.Safari()
    
    # Make its calls wait up to 10 sec for elements to apear
    b.implicitly_wait(10)
    
    # Return the WebDriver instance
    yield b
    
    # Quit the WebDriver instance for the cleanup
    b.quit()