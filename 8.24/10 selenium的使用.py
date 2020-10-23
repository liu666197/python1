from selenium import webdriver

# 指定对应的浏览器访问网页
# driver: 浏览器
driver = webdriver.Chrome('chromedriver.exe')
# url
url = 'https://www.zcool.com.cn/'
# 打开网页
driver.get(url)
# 获取源代码: driver.page_source
print(driver.page_source)
with open('1.html','w',encoding='utf-8') as file:
    file.write(driver.page_source)
# 关闭浏览器
driver.quit()