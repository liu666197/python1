# file = open('笔记,txt','r',encoding='utf-8')
# file.close()

with open('笔记.txt','r',encoding='utf-8') as file:
    print(file.read())

with open('2.txt','w',encoding='utf-8') as file:
    file.write('2222')

# a = [1,2,3]
# a.append(4)
# a.append(5)
# print(a)