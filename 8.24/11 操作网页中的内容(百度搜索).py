from selenium import webdriver
import time
# 指定对应的浏览器访问网页
# driver: 浏览器
driver = webdriver.Chrome('chromedriver.exe')
# 1.打开网页
url = 'https://www.baidu.com/'
driver.get(url)
# 找到对应的标签,再进行相应的操作(事件)
# 右击对应网页内容,检查,找到对应标签,右击-->copy --> copy xpath
# send_keys(value): 往输入框里面添加
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('aaa')
# 找到按钮,点击按钮
# click: 点击
driver.find_element_by_xpath('//*[@id="su"]').click()
# 停留一会
time.sleep(2)
with open('百度.html','w',encoding='utf-8') as file:
    file.write(driver.page_source)

# 停留一会
time.sleep(2)
# 关闭浏览器
driver.quit()