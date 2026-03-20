from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = opts)
driver.maximize_window()
print("Browser started")

sites = [
    "https://www.nike.com/in",
    "https://www.bewakoof.com/",
    "https://www.bbc.com/news",
    "https://www.python.org"
]

for site in sites:
    sleep(3)
    driver.get(site)
    print("Page Title:", driver.title)
    print()

sleep(3)
driver.quit()