import csv
# 属性
a = 10
# 方法
def sayHello():
    print('hello')

# user-agent列表
userAgentList = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'
]

def saveFile(filename,header,count,dic):
    with open(filename, 'a', encoding='utf-8-sig', newline='') as file:
        # 写入者
        csv_file = csv.DictWriter(file, header)
        if count == 1:
            # 写入表头(第一条数据的时候写入表头)
            csv_file.writeheader()
        # 写入所有数据
        csv_file.writerow(dic)

print('++++',__name__)
if __name__ == '__main__':
    # 自己运行的时候,代码生效
    print('当前py文件运行')