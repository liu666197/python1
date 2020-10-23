# 直接给程序员进行提醒
# try:
#     a = 10 / 0
#     print(a)
# except:
#     # 只有当程序崩溃的时候才会执行
#     print('程序出现问题,请核对代码')

# 想知道异常的原因
# try:
#     a = 10 / 0
#     print(a)
# except Exception as e:
#     print('程序出现问题,请核对代码',e)
try:
    a = int(input('请输入一个数字: '))
    print(a)
except:
    print('请输入正确的数字...')
    print('请按照规则输入')