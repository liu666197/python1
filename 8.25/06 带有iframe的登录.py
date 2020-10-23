from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://mail.163.com/')
# 一般登录页面所用的标签在iframe标签或者frame标签
# 找到对应的iframe标签
iframe = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
# 得先将driver指向嵌套的网页(iframe)
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@name="email"]').send_keys('abchuayanghai')
driver.find_element_by_xpath('//*[@name="password"]').send_keys('hai*98765432')
driver.find_element_by_xpath('//*[@id="dologin"]').click()
time.sleep(5)
with open('163.html','w',encoding='utf-8') as file:
    file.write(driver.page_source)
