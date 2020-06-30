from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 测试通过cookie绕开验证码登陆公司邮箱

url = "https://mail.bonc.com.cn/"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(By.ID, "uid").send_keys("zhangshilin@bonc.com.cn")
driver.find_element(By.ID, "password").send_keys("305424820@ab")

time.sleep(10)
driver.find_element(By.ID, "login_button").click()

# 首次登陆后获取cookie
cookie_list = driver.get_cookies()

print(cookie_list)
driver.find_element(By.ID, "navFid_1").click()

driver.quit()

time.sleep(10)

# 再次登陆
driver = webdriver.Chrome()

driver.get("https://mail.bonc.com.cn/")
url1 = ""

url1 = url + "coremail/XT3/index.jsp?sid=" + cookie_list[0]['value'] #需在url中添加cookie中的"Coremail.sid"项
driver.add_cookie({'name': cookie_list[0]['name'], 'value': cookie_list[0]['value']})
driver.add_cookie({'name': cookie_list[1]['name'], 'value': cookie_list[1]['value']})
driver.add_cookie({'name': cookie_list[2]['name'], 'value': cookie_list[2]['value']})
driver.add_cookie({'name': cookie_list[3]['name'], 'value': cookie_list[3]['value']})
driver.add_cookie({'name': cookie_list[4]['name'], 'value': cookie_list[4]['value']})
driver.get(url1)
