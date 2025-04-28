from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your ChromeDriver
chromedriver_path = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Chrome options (optional)
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver
service = Service(chromedriver_path)    
# driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome(service=service)

try:
    # Open the Wi-Fi login page
    wifi_login_url = "http://phc.prontonetworks.com/cgi-bin/authlogin"  # Replace with the actual login page URL
    driver.get(wifi_login_url)

    # Wait for the page to load
    time.sleep(1)

    # Fill in the username
    username_field = driver.find_element(By.NAME, "userId")  # Update "username" with the correct field name
    username_field.send_keys("24BBS0033")

    # Fill in the password
    password_field = driver.find_element(By.NAME, "password")  # Update "password" with the correct field name
    password_field.send_keys("0033")

    # Submit the form (click Login or press Enter)
    login_button = driver.find_element(By.NAME, "Submit22")  # Update "login_button" with the correct element ID
    login_button.click()

    # Wait for login to complete
    time.sleep(1)

    # Verify login success
    if "Success" in driver.page_source:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    # Close the browser
    driver.quit()
#-------------------------------------------------------------------------------------
# import requests

# # Wi-Fi login page URL
# login_url = "http://wifi-login-page.url"

# # Login credentials
# payload = {
#     "username": "your_username",
#     "password": "your_password"
# }

# # Send the login request
# response = requests.post(login_url, data=payload)

# # Check the response
# if response.status_code == 200 and "Success" in response.text:
#     print("Login successful!")
# else:
#     print("Login failed!")
#-------------------------------------------------------------------------------------------------
