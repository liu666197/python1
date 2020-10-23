from selenium import webdriver
# mac: chromedriver的路径使用绝对路径: C:\Users\Master\Desktop\python\8.25\chromedriver.exe
driver = webdriver.Chrome('chromedriver.exe')

# with open('1.html','w',encoding='utf-8') as file:
#     # 源代码: driver.page_source
#     file.write(driver.page_source)
# 第一页: driver.page_source

# # 第二页
# driver.find_element_by_xpath('//*[@id="istj"]//a[@class="next"]').click()
# print(driver.page_source)
#
# # 第三页
# driver.find_element_by_xpath('//*[@id="istj"]//a[@class="next"]').click()
# print(driver.page_source)
for i in range(1,10):
    print('第{}页开始'.format(i))
    if i == 1:
        driver.get('https://www.zhisheji.com/')
    else:
        driver.find_element_by_xpath('//*[@id="istj"]//a[@class="next"]').click()
    # 解析数据: driver.page_source
    print('第{}页结束'.format(i))