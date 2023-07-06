from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://github.com"

driver.get(url)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-home page.png")

url = "http://github.com/ugurfatihcokuckun"
driver.get(url)

print(driver.title)

if "ugurfatihcokuckun" in driver.title:
    driver.save_screenshot("github-ugurfatihcokuckun.png")

time.sleep(2)
driver.back()
# driver.forward()
time.sleep(2)
driver.close()