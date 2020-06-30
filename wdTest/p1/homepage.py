"""
截图
测试环境：baidu
"""

from selenium import webdriver
import time

url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
# 超时设置
driver.implicitly_wait(10)


def screen_shot(driver):
    driver.get_screenshot_as_file("test.png")


screen_shot(driver)
