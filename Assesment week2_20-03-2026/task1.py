# Open Amazon
#
# Verify page title and current URL
#
# Locate the category dropdown (next to search bar)
#
# Select "Books" using Select class
#
# Enter "Harry Potter" in search and press Enter
#
# Use explicit wait to wait until results are visible
#
# Get all product titles using find_elements
#
# Print first 5 product names
#
# Click on the first product


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = opts)
driver.maximize_window()

driver.get("https://www.amazon.com/")


if driver.current_url == "https://www.amazon.com/":
    print("Verified")



wait = WebDriverWait(driver, 10)


category =wait.until(EC.presence_of_element_located((By.XPATH,"//select[@class='nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown']")))

select=Select(category)

select.select_by_visible_text('Books')




search=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='twotabsearchtextbox']")))

search.send_keys("Harry Potter",Keys.ENTER)

wait.until(EC.presence_of_all_elements_located((By.XPATH,"//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")))

sleep(5)

all_products = driver.find_elements(By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']/span")

print('\nPrint first 5 products')

for i in range (0,5):

    print(i+1,all_products[i].text)

all_products[0].click()

driver.quit()

