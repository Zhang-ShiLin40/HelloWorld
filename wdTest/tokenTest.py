from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()

browser.get("https://mail.bonc.com.cn/")
browser.get("https://mail.bonc.com.cn/")
browser.find_element(By.ID, "uid").send_keys("zhangshilin@bonc.com.cn")
browser.find_element(By.ID, "password").send_keys("305424820@ab")

time.sleep(10)
browser.find_element(By.ID, "login_button").click()

time.sleep(3)

#获取token
token = browser.execute_script('window.localStorage.getItem("token")')
print(token)
#添加token
#js=window.localStorage.setItem("token","token值")
#browser.execute_script(js)

#browser.refresh()#刷新
