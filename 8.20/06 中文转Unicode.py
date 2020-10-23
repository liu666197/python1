import urllib.parse
# decode: 解码(转化为我们认识的)  encode: 编码(转化为我们不认识的)
# urllib.parse.urlencode(字典)
dic = {
    'wd': '哈哈哈'
}
# 转换
result = urllib.parse.urlencode(dic)
print(type(result),result)