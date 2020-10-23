import string
print(string.punctuation)
#
# try:
#     a = 'aaa'
#     print(int(a))
# except:
#     print('不能是字母或者汉字')

a = [123,123,12,342,423,4]
# count: 出现次数 > 1
for i in a:
    count = a.count(i)
    if count > 1:
        print('重复')
        break
