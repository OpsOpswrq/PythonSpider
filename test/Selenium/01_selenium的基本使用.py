from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
s = Service(executable_path=r'../driver/msedgedriver.exe')
browser = webdriver.Edge(service=s)
url = 'https://www.baidu.com'
browser.get(url)
button = browser.find_element(By.ID,"su")
input = browser.find_element(By.NAME,'wd')
xpath = browser.find_element(By.XPATH,'//input[@id="su"]')
tag = browser.find_element(By.TAG_NAME,'input')
link = browser.find_element(By.LINK_TEXT,'视频')
print(button)
print(input)
print(xpath)
print(tag)
print(link)
time.sleep(3)
browser.quit()