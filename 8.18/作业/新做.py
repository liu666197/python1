# 4.将zhanku.html放在pycharm打开,然后取出每条数据的 作品图片url地址,作品名字,作品类型,人气数,评论数,点赞数,作者
# 如果没有该字段的数据,写无;把数据存入到csv
# 作品图片的url地址: <img src="图片的地址">
import re
# 读取站酷里的内容,打开zhanku.html,点击空白的地方用谷歌搜索,点击图片查找图片的'检查',
# 将结果复制zhanku.html查找原代码
with open('zhanku.html','r',encoding='utf-8') as file:
    content = file.read()
# 制定规则
# 图片的url地址.有问题
# 图片1
#  target="_blank" z-st="home_main_card_cover">
#             <img src="https://img.zcool.cn/community/0155075f3a9950a80120a8211ebc84.jpg@260w_195h_1c_1e_1o_100sh.jpg"
#                  srcset="https://img.zcool.cn/community/0155075f3a9950a80120a8211ebc84.jpg@520w_390h_1c_1e_1o_100sh.jpg 2x"
#                  title="【打开新视界，享受多彩生活】蔡司包装设计" alt="">
# 图片2
#   target="_blank" z-st="home_main_card_cover">
#             <img src="https://img.zcool.cn/community/01926b5f3b32f2a801215aa029cead.jpg@260w_195h_1c_1e_1o_100sh.jpg"
#                  srcset="https://img.zcool.cn/community/01926b5f3b32f2a801215aa029cead.jpg@520w_390h_1c_1e_1o_100sh.jpg 2x"
#                  title="【绿衣女】" alt="">
# 根据所找到的内容进行比对,需要匹配的的内容用(.+?)
# pattern = '''target="_blank" z-st="home_main_card_cover">
#             <img src="(.+?)"
#                  srcset=".+?"
#                  title="(.+?)" alt="">'''
# pattern=r'(target="_blank" z-st="home_main_card_cover"><img src="(.+?)"srcset=".+?"title="(.+?)" alt="">)'
# result = re.findall(pattern,content,re.S)
# print(len(result))
# pattern = r'<p class="card-info-type" title="(.+?)">'
# typeResult = re.findall(pattern,content,re.S)
# print(typeResult,len(typeResult)) g
# 作品类型
# <p class="card-info-type" title="平面-包装">平面-包装</p>
# < p class ="card-info-type" title="摄影-手机" > 摄影-手机 < / p >
# pattern=r'<p class="card-info-type" title=(.+?)</p>'
# typeResult = re.findall(pattern,content,re.S)
# print(typeResult,len(typeResult))
# 人气数(38)
#  <span class="statistics-view" title="共9982人气">9982</span>
# < span class ="statistics-view" title="共11545人气" > 1.2w < / span >
# pattern=r'<span class="statistics-view" title="共(.+?)人气">'
# fansResult=re.findall(pattern,content,re.S)
# print(fansResult ,len(fansResult ) )
# 评论数.有问题
# < span class ="statistics-comment" title="共60评论" > 60 < / span >
# < span class ="statistics-comment" title="共10评论" > 10 < / span >
# pattern =r'<span class ="statistics-comment" title="共(.+?)评论" >'
# pinglunResult = re.findall(pattern,content,re.S)
# print(pinglunResult,len(pinglunResult))
# 点赞
#  <span class="statistics-tuijian" title="共252推荐">
# < span class ="statistics-tuijian" title="共70推荐" >
# pattern=r'<span class="statistics-tuijian" title="共(.+?)推荐">'
# dianzanResult = re.findall(pattern,content,re.S)
# print(dianzanResult,len(dianzanResult))
# 作者
# <a href="https://startalk.zcool.com.cn" title="STARTALK星话" target="_blank" z-st="home_main_card_user">
# <a href="https://thomaskksj.zcool.com.cn" title="thomas看看世界" target="_blank" z-st="home_main_card_user">
pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)'
result = re.findall(pattern,content,re.S)
print(result,len(result))
  