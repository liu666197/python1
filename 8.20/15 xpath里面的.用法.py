from lxml import etree

with open('4.html','r',encoding='utf-8') as file:
    content = file.read()

# 把字符串转化为标签对象
html = etree.HTML(content)
print(html)
# 标签对象.xpath
result = html.xpath('//div')[0]
# result: div标签对象 从当前的div标签里面查找
# result = result.xpath('./a/text()')
result = result.xpath('.//a/text()')
print(result)