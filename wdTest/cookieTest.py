from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://mail.bonc.com.cn/"
driver = webdriver.Chrome()
driver.get(url)

cookie_list = [{'domain': 'mail.bonc.com.cn', 'httpOnly': False, 'name': 'Coremail.sid', 'path': '/', 'secure': False, 'value': 'BAaphcllROEAUaygkKllaoFIfcWzOyGN'},
               {'domain': 'mail.bonc.com.cn', 'httpOnly': False, 'name': 'CoremailReferer', 'path': '/', 'secure': False, 'value': 'https%3A%2F%2Fmail.bonc.com.cn%2F'},
               {'domain': 'mail.bonc.com.cn', 'httpOnly': True, 'name': 'Coremail', 'path': '/', 'secure': False, 'value': '017816746efd7968836e8a037c2626d5'},
               {'domain': 'mail.bonc.com.cn', 'expiry': 4105008000, 'httpOnly': False, 'name': 'locale', 'path': '/', 'secure': False, 'value': 'zh_CN'},
               {'domain': 'mail.bonc.com.cn', 'expiry': 4105008000, 'httpOnly': False, 'name': 'uid', 'path': '/', 'secure': False, 'value': 'zhangshilin@bonc.com.cn'}]


driver = webdriver.Chrome()

driver.get("https://mail.bonc.com.cn/")
url1 = ""
# for cookie in cookie_list:
#    driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
#   if cookie['name'] == 'Coremail.sid':

url1 = url + "coremail/XT3/index.jsp?sid=" + cookie_list[2]['value']
driver.add_cookie({'name': cookie_list[0]['name'], 'value': cookie_list[0]['value']})
driver.add_cookie({'name': cookie_list[1]['name'], 'value': cookie_list[1]['value']})
driver.add_cookie({'name': cookie_list[2]['name'], 'value': cookie_list[2]['value']})
driver.add_cookie({'name': cookie_list[3]['name'], 'value': cookie_list[3]['value']})
driver.add_cookie({'name': cookie_list[4]['name'], 'value': cookie_list[4]['value']})
driver.get(url1)
