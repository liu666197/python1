# 4.将zhanku.html放在pycharm打开,然后取出每条数据的 作品图片url地址,作品名字,作品类型,人气数,评论数,点赞数,作者
# 如果没有该字段的数据,写无;把数据存入到csv
# 作品图片的url地址: <img src="图片的地址">
import re
# 读取站酷里的内容,打开zhanku.html,点击空白的地方用谷歌搜索,点击图片查找图片的'检查',
# 将结果复制zhanku.html查找原代码
with open('zhanku.html','r',encoding='utf-8') as file:
    content = file.read()
# 制定规则
# 图片的url地址,例如
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
pattern = '''target="_blank" z-st="home_main_card_cover">
            <img src="(.+?)"
                 srcset=".+?"
                 title="(.+?)" alt="">'''
pattern=r'(target="_blank" z-st="home_main_card_cover"><img src="(.+?)"srcset=".+?"title="(.+?)" alt="">)'
result = re.findall(pattern,content,re.S)
print(len(result))