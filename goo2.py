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








from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
options = Options()
driver = webdriver.Edge(options=options)
driver.get("https://www.google.com")
time.sleep(50)
search_box = driver.find_element(By.NAME, "q")
print("Tag Name:", search_box.tag_name)
print("Element Text:", search_box.text)
print("Displayed:", search_box.is_displayed())
print("Enabled:", search_box.is_enabled())
print("Outer HTML:", search_box.get_attribute("outerHTML"))
time.sleep(5)
driver.quit()





docker --version
docker pull ubuntu
docker images
docker run ubuntu
docker ps
docker ps -a
docker stop <container_id>
docker rm <container_id>
docker rmi ubuntu





