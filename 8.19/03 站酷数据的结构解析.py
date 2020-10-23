import re,csv
# import csv
with open('zhanku.html','r',encoding='utf-8') as file:
    # 整个网页的源代码
    content = file.read()

# 规则
# 图片url地址
# pattern = '''target="_blank" z-st="home_main_card_cover">
#             <img src="(.+?)"
#                  srcset=".+?"
#                  title="(.+?)" alt="">'''
# 38条
# pattern = r'target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">'
# 2条
# pattern = r'z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">'

# 保证数据的顺序不变
pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
# 从源代码里面取图片url地址
# 返回值: 列表
result = re.findall(pattern,content,re.S)
print(len(result))
count = 0
# 所有的url地址
urlResult = []
# 所有的作品名字
titleResult = []
# 取出数据
for i in result:
    count += 1
    # print(count)
    # print(i[1],i[2])
    # print(i[4],i[5])
    # 当第1条-第4条没有值的时候
    url = i[1] or i[4]
    title = i[2] or i[5]
    urlResult.append(url)
    titleResult.append(title)
    # print(i)
print(len(urlResult),len(titleResult))
# 作品类型
pattern = r'<p class="card-info-type" title="(.+?)">'
typeResult = re.findall(pattern,content,re.S)
# print(typeResult,len(typeResult))
# 人气数 (38)
pattern = r'<span class="statistics-view" title="共(.+?)人气">'
fansResult = re.findall(pattern,content,re.S)
# print(fansResult,len(fansResult))
# 评论数
pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
pinglunResult = re.findall(pattern,content,re.S)
# print(pinglunResult,len(pinglunResult))
# 点赞数
pattern = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
dianzanResult = re.findall(pattern,content,re.S)
print(dianzanResult,len(dianzanResult))
# 作者(38)
# pattern = r'<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">'
# (2)
# pattern = r'class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">'

pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)'
result = re.findall(pattern,content,re.S)
# 40条
authorResult = []
count = 0
for i in result:
    count += 1
    author = i[1] or i[3]
    authorResult.append(author)

# 凑数据  关于第五条(下标为4)和第四十条(39)数据,点赞数,评论数,人气数 无
# fansResult.insert(4,'无')
# fansResult.insert(39,'无')
# pinglunResult.insert(4,'无')
# pinglunResult.insert(39,'无')
# dianzanResult.insert(4,'无')
# dianzanResult.insert(39,'无')
def insertData(a):
    a.insert(4, '无')
    a.insert(39, '无')
insertData(fansResult)
insertData(pinglunResult)
insertData(dianzanResult)

count = 0
# 所有的结果
allResult = []
# 凑成一个个字典
for i in range(40):
    count += 1
    print(count)
    # url的数据
    # 1个字典的数据
    dic = {
        'url地址': urlResult[i],
        '作品名': titleResult[i],
        '作品类型': typeResult[i],
        '人气数': fansResult[i],
        '评论数': pinglunResult[i],
        '点赞数': dianzanResult[i],
        '作者': authorResult[i]
    }
    allResult.append(dic)

# 表头
header = ['url地址','作品名','作品类型','人气数','评论数','点赞数','作者']

# 存入csv
with open('站酷.csv','w',encoding='utf-8-sig',newline='') as file:
    # 写入者
    csv_file = csv.DictWriter(file,header)
    # 写入表头
    csv_file.writeheader()
    # 写入所有数据
    csv_file.writerows(allResult)






