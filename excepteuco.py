from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
driver = webdriver.Chrome(options=options)
driver.get('https://www.example.com