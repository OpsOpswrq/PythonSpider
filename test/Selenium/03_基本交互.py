from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
s = Service(executable_path=r'../driver/msedgedriver.exe')
browser = webdriver.Edge(service=s)
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(2)
browser.save_screenshot("baidu.png")
input = browser.find_element(By.NAME,'wd')
input.send_keys('喜多川海梦')
time.sleep(2)
button = browser.find_element(By.ID,'su')
button.click()
time.sleep(2)
js = "document.documentElement.scrollTop=100000"
browser.execute_script(js)
time.sleep(2)
next = browser.find_element(By.XPATH,'//a[@class="n"]')
next.click()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(3)
browser.quit()