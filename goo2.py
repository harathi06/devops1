from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.google.com")

driver.find_element(By.NAME, "q")
driver.find_element(By.NAME, "btnK")

print("Elements found successfully")

driver.quit()






from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.facebook.com")

driver.find_element(By.ID, "email").send_keys("your_email")
driver.find_element(By.ID, "pass").send_keys("your_password")
driver.find_element(By.NAME, "login").click()

time.sleep(50)

time.sleep(50)
driver.quit()








from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,"q")
print("Element found:",search_box)
driver.quit()