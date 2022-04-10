from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
s = Service(executable_path=r'../driver/msedgedriver.exe')
browser = webdriver.Edge(service=s)
url = 'https://www.baidu.com'
browser.get(url)
button = browser.find_element(By.ID,"su")
print(button.get_attribute("value"))
print(button.tag_name)
link = browser.find_element(By.LINK_TEXT,"视频")
print(link.text)
time.sleep(3)
browser.quit()