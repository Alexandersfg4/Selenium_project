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
```
Paste your Creds inside data_file.py

## How to run
```zsh
# Run all test cases
pytest -v
```
## Implemented test cases
I have named test files based on functionality
<br> **login.py** contains the next test cases: </br>
<br>1. *test_basic_login*
<br>Steps: 
- Open the main page
- Fill out username and password
- Click on "Log In" button
<br> Excepted result:
    - Oppened home page
    - Shown button bar
    - On the center shown search bar
    - Shown dialog "Save Your Login Info?"
<br> Excepted result: status code = 200, Json response = data sent on step 1 </br>