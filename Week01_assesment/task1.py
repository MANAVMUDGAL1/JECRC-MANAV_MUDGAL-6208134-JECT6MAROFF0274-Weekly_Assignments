from h5py import ExternalLink
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
Username=driver.find_element(By.CSS_SELECTOR ,"input[name='username']")
print(Username)

Password=driver.find_element(By.CSS_SELECTOR ,"input[id='password']")
print(Password)

Submit_button=driver.find_element(By.CSS_SELECTOR ,"button[type='submit']")
print(Submit_button.text)

external_link=driver.find_element(By.CSS_SELECTOR ,"div[style='text-align: center;'] a")
print(external_link.text)

