#!/usr/bin/env python3
"""
"""
from selenium import webdriver

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# path = "/mnt/c/chromedriver.exe"
# driver = webdriver.Chrome()

# driver.get("https://www.jacknjenga.tech")
# driver.quit()

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = "/mnt/c/Users/dell/AppData/Local/Google/Chrome/Application/chrome.exe"

options = Options()
options.add_experimental_option("detach", True)
options.binary_location = chrome_path

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.neuralnine.com/")
