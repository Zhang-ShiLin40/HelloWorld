"""
鼠标事件，右键，双击
测试环境：ETL
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

url = "http://172.16.43.170:9979/view/login/index.html"
driver = webdriver.Chrome()
driver.get(url)
# 超时设置
driver.implicitly_wait(10)

# 登陆
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/input").send_keys("zhangshilin")
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/input").send_keys("a1234567")
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/button").click()

#time.sleep(5)

# 进入项目列表
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div/a/span").click()
# 进入项目首页
driver.find_element(By.PARTIAL_LINK_TEXT, "zsltest0415").click()
# 进入工作流定义页
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[3]/div/ul/li[1]/span").click()
# 进入工作流画布
driver.find_element(By.PARTIAL_LINK_TEXT, "zsltest0415-1").click()

ico = driver.find_element(By.XPATH, "//*[@id=\"tasks-54188\"]/div[1]/div[2]")

# 右键
# ActionChains(driver).context_click(ico).perform()

# 双击
ActionChains(driver).double_click(ico).perform()
# driver.find_element(By.XPATH, "").click()
