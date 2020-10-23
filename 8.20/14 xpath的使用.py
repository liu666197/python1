from lxml import etree

# a = '<a href="#">新闻1</a><a href="#" class="b">新闻2</a><a href="#">新闻3</a><a href="#">新闻4</a>'
#
# # 源代码(字符串)
# # 1.将源代码的字符串类型转化为html的元素(标签对象)
# html = etree.HTML(a)
# # 2.写xpath: //a/text()
# # 格式: 标签对象.xpath(xpath语句) 结果是个列表
# # result = html.xpath('//a/text()')
# result = html.xpath('//a[@class="b"]/text()')
# print(result)
# with open('1.html','r',encoding='utf-8') as file:
#     content = file.read()
# # 1.将源代码的字符串类型转化为html的元素(标签对象)
# html = etree.HTML(content)
# # 2.使用xpath
# # 取双标签内容
# result1 = html.xpath('//div/a/text()')
# # 取属性值
# result2 = html.xpath('//div/a/@href')
# print(result1,result2)

with open('2.html','r',encoding='utf-8') as file:
    content = file.read()
# 1.将源代码的字符串类型转化为html的元素(标签对象)
html = etree.HTML(content)
# title = html.xpath('//div[@class="card-box"]/div/a/img/@title')
title = html.xpath('//div[@class="card-box"]//img/@title')
print(title)
