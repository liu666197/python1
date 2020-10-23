from lxml import etree
a = """<a href="#" class="a" title="1">新闻1</a><a href="#" class="b" title="1">新闻2</a><a href="#" title="1">新闻3</a><a href="#">新闻4</a>"""
html = etree.HTML(a)
# result = html.xpath('//a[3]/text()')
# result = html.xpath('//a[@class="a"]/text()')
# result = html.xpath('//a[@class="b"]/text()')
# result = html.xpath('//a[@class="a" or @class="b"]/text()')
# result = html.xpath('//a[@title="1" and @class="a"]/text()')
result = html.xpath('//a[not (@class="a")]/text()')
print(result)
