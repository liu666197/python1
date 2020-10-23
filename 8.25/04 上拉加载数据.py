from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%BD%A9%E5%A5%87')
# 运行javascript代码
# driver.execute_script('alert(1);')
with open('1.html','a',encoding='utf-8') as file:
    file.write(driver.page_source.replace('&amp;','&'))
for i in range(10):
    # 滚动一屏
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # driver.page_source: 滚动一屏以后的源代码
    with open('1.html', 'a', encoding='utf-8') as file:
        file.write(driver.page_source)