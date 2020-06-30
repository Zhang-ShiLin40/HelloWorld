from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# 测试通过cookie绕开验证码登陆公司邮箱

url = "http://172.16.43.170:7676/dist/#/login"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/form/div[1]/div/div/input")\
    .send_keys("zhangshilin")
driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/form/div[2]/div/div[1]/input")\
    .send_keys("a1234567")

time.sleep(10)
driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[2]/form/button").click()
time.sleep(3)
# 首次登陆后获取cookie
cookie_list = driver.get_cookies()
time.sleep(3)
print(cookie_list)

with open("cookie.csv", "w") as fw:
    writer = csv.writer(fw)
    for cookie in cookie_list:
        writer.writerow([cookie['name'], cookie['value']])
time.sleep(3)
token = driver.execute_script('return sessionStorage.getItem("token");')

print(token)
#with open("token.csv", "w") as fw:
 #   writer = csv.writer(fw)
 #   writer.writerow(token)
#driver.find_element(By.ID, "navFid_1").click()

driver.quit()
