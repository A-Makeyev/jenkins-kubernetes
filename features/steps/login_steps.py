from behave import *
from selenium import webdriver

@given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'open orange hrm homepage')
def open_home_page(context):
    context.driver.get('https://www.orangehrm.com/')
    

@then(u'verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath('(//img[@alt="OrangeHRM Logo"])[1]').isDisplayed()
    assert status is True

@then(u'close browser')
def close_browser(context):
    context.driver.close()
    
    
#     from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @given('launch chrome browser')
# def launch_browser(context):
#     service = Service(ChromeDriverManager().install())
#     context.driver = webdriver.Chrome(service=service)

# @when('open orange hrm homepage')
# def open_home_page(context):
#     context.driver.get('https://www.orangehrm.com/')

# @then('verify that the logo present on page')
# def verify_logo(context):
#     # Use WebDriverWait to ensure the element is loaded
#     logo = WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '(//img[@alt="OrangeHRM Logo"])[1]'))
#     )
#     assert logo.is_displayed() is True

# @then('close browser')
# def close_browser(context):
#     context.driver.quit()  # safer than close()
