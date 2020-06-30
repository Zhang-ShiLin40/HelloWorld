import csv

# 将cookie写入csv

cookie_list = [{'domain': 'mail.bonc.com.cn', 'httpOnly': False, 'name': 'Coremail.sid', 'path': '/', 'secure': False,
               'value': 'BAophcllUVdAUabDBKllmVbPOwrZwmLN'},
              {'domain': 'mail.bonc.com.cn', 'httpOnly': False, 'name': 'CoremailReferer', 'path': '/', 'secure': False,
               'value': 'https%3A%2F%2Fmail.bonc.com.cn%2F'},
              {'domain': 'mail.bonc.com.cn', 'httpOnly': True, 'name': 'Coremail', 'path': '/', 'secure': False,
               'value': 'fb5e2530839eb9affc39e3409cf43052'},
              {'domain': 'mail.bonc.com.cn', 'expiry': 4105008000, 'httpOnly': False, 'name': 'locale', 'path': '/',
               'secure': False, 'value': 'zh_CN'},
              {'domain': 'mail.bonc.com.cn', 'expiry': 4105008000, 'httpOnly': False, 'name': 'uid', 'path': '/',
               'secure': False, 'value': 'zhangshilin@bonc.com.cn'}]

with open("../test1.csv", "a") as fw:
    writer = csv.writer(fw)
    for cookie in cookie_list:
         writer.writerow([cookie['name'], cookie['value']])
#    driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
#   if cookie['name'] == 'Coremail.sid':
