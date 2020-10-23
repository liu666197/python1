from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('1104781249@qq.com')
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('hai*98765432')

# 用户输入验证码(手机验证码,图形验证码)
code = input('请输入验证码: ')
driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
# 点击
driver.find_element_by_xpath('//*[@id="denglu"]').click()
with open('1.html','w',encoding='utf-8') as file:
    file.write(driver.page_source)

