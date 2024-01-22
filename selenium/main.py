from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# chrome_driver_path = "C:/Program Files (x86)/chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")

# while True:
#     pass