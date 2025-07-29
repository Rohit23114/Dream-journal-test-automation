from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://arjitnigam.github.io/myDreams/"
WAIT_TIMEOUT = 10

def get_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver

def get_wait(driver):
    return WebDriverWait(driver, WAIT_TIMEOUT)
