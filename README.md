# WEB automation project 
Test web application: https://www.instagram.com/ 

## Purpose
1. To implement working project based on https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/chapter1.html<br>
2. To build a basic Web UI test automation solution using Python and Selenium WebDriver

## Setup

```zsh
# Activate venv
souce env/bin/activate
# Install all dependencies in your virtualenv
pip install -r requirements.txt 
# Paste your creds inside test/data/test_data.json
{
    "config":
    {
        "browser": "Headless Chrome",
        "implicit_wait": 10
    }
    ,
    "valid_user_data":
    {
        "login": "test@test.com",
        "password": "password"
    }
}
```


## How to run
```zsh
# Run all test cases
pytest -v
```
## Implemented test cases
I have named test files based on functionality
<br> **test_login.py** contains the next test cases: </br>
<br>1. *test_basic_login*
<br>**Steps:** 
- Open the main page
- Fill out username and password
- Click on "Log In" button
<br> **Excepted result**:
    - Oppened home page
    - Shown button bar
    - On the center shown search bar
    - Shown dialog "Save Your Login Info?" <br>

<br>2. *test_login_invalid_data*
<br>**Steps:** 
- Open the main page
- Fill out  username and invalid password
- Click on "Log In" button
<br> **Excepted result**:
    - Shown error message  