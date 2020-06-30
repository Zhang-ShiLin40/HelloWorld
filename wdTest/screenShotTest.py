"""
截图
测试环境：baidu
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
# 超时设置
driver.implicitly_wait(10)

# 截图，将图片存储到指定文件夹
driver.get_screenshot_as_file("img/test7.png")
