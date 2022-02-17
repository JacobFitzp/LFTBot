from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import config

print('''
-----------------
LFT Bot Started
-----------------
''')

print("> Logging In...")

driver_options = Options()
driver_options.add_argument('--headless')
driver_options.add_argument('--no-sandbox')

driver_service = Service(config.driver_path)

driver = webdriver.Chrome(service=driver_service, options=driver_options)

driver.implicitly_wait(30)

# Begin Journey
driver.get('https://www.gov.uk/order-coronavirus-rapid-lateral-flow-tests')

# Start Order
driver.find_element(By.CLASS_NAME, 'govuk-button--start').click()
driver.find_element(By.ID, 'condition-2').click()
driver.find_element(By.CSS_SELECTOR, '#main-content form button').click()

# Login
driver.find_element(By.CLASS_NAME, 'govuk-button--secondary').click()
driver.find_element(By.ID, 'user-email').send_keys(config.account_details['email'])
driver.find_element(By.CSS_SELECTOR, '#main-content button').click()

time.sleep(config.page_delay)

if driver.current_url == 'https://access.login.nhs.uk/register/account-creation-alert':
    print("  └ Login Failed")
    exit()

if driver.current_url == 'https://access.login.nhs.uk/existing-account-alert':
    driver.find_element(By.CSS_SELECTOR, '#main-content button').click()

time.sleep(config.page_delay)

driver.find_element(By.ID, 'password-input').send_keys(config.account_details['password'])
driver.find_element(By.CSS_SELECTOR, '[data-qa="enter-password-submit-button"]').click()

time.sleep(config.page_delay)

if driver.current_url == 'https://access.login.nhs.uk/log-in-password':
    print("  └ Login Failed")
    exit

print("  └ Login Successful")

print("> Placing Order...")

# Employee Program
driver.find_element(By.ID, 'nhs-staff-2').click()
driver.find_element(By.CSS_SELECTOR, '#main-content form button').click()

# Confirm Details
driver.find_element(By.CSS_SELECTOR, '#main-content button[type="submit"]').click()

time.sleep(config.page_delay)

# Cannot place order
if driver.title == 'There was a problem - Coronavirus Home Testing - GOV.UK':
    print("  └ Order Failed")
    print("    └ Previous order placed in the last 24 hours")
    driver.close()
    exit()

# Place Order
driver.find_element(By.CSS_SELECTOR, 'input[name="disclaimer"]').click()
driver.find_element(By.CSS_SELECTOR, '#main-content button').click()

time.sleep(config.page_delay)

print("  └ Order Placed")

driver.close()
