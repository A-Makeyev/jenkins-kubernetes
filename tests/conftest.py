import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup():
    options = Options()

    if os.getenv('CI', 'false').lower() == 'true':
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
