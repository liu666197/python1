from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')

driver.get('http://news.baidu.com/')
# 浏览器指向的当前网址
# print(driver.current_url)
# 当前浏览器打开的窗口
# print(driver.window_handles)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="pane-news"]/ul[1]/li[5]/a').click()
# 切换driver的窗口指向 (窗口名)
driver.switch_to.window(driver.window_handles[1])
# 当前浏览器打开的窗口
# print(driver.window_handles)
with open('新闻.html','w',encoding='utf-8') as file:
    file.write(driver.page_source)