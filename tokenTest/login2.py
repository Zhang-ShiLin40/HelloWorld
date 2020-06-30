from selenium import webdriver

cookie_list = [{'domain': '172.16.43.170', 'httpOnly': False, 'name': 'Admin-Token', 'path': '/', 'secure': False,
                'value': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ6aGFuZ3NoaWxpbiIsInVzZXJJZCI6IjIwNCIsIm5hbWUiOiLlvKDor5fnkLMiLCJleHAiOjE1ODcxMDQyMzZ9.03UXM-DWNPWb2fKLaYTClC-w5U4dCNCI69xcFG1DBdUXVcYgqs4hkstF2tetwOZmuxzMWWMsYn6fhitbUJCpmtapsB9lr57UJUShCV9j8kH-5pZxhkdwsFazim7SMEk51s2iVg37bmzEjOv14QtGfFjZnT2aUAPJEAqh4bkY-0NDWevcK-vig-A5nE3mid2qIfEKaZZ0hUgtEx-TZkyu9wIcPuenfNUWRFam9mpUZnLj-1N3gJz8z0y6Ydkn9kFew7V95L3qopctAYZOm8l2r8cm6E4Jcxduxs_S7L-Yg1zFV8tE7FC64imqd_cKG1QweqUJUGi8OX0i9lt_SoqRFA'},
               {'domain': '172.16.43.170', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False,
                'value': '5C78C100D42F063E117F56778E3B319F'}]

url = "http://172.16.43.170:7676/dist/#/login"
driver = webdriver.Chrome()
driver.get(url)

driver.add_cookie({'name': cookie_list[0]['name'], 'value': cookie_list[0]['value']})
driver.add_cookie({'name': cookie_list[1]['name'], 'value': cookie_list[1]['value']})

driver.refresh()
