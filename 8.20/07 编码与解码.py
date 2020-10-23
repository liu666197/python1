# 二进制数据: b''  (bytes类型)
# a = b'hello world'
# # 解码: 将二进制转字符串
# result = a.decode()
# print(a,type(a))
# print(result,type(result))

# 编码: 将字符串转二进制数据
a = 'hello world 中文'
result = a.encode('utf-8')
print(result,type(result))
result = result.decode('utf-8')
print(result)