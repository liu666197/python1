
while True:
    shuru = input('请输入你要喷的内容: ')
    # 停止
    if shuru in 'qQ':
        # 停止整个循环
        break
    # 不良信息
    if '你大爷的' in shuru:
        print('你当前输入的内容含有敏感词汇,请重新输入')
        # 中止某次循环,但是整个循环还会继续执行
        continue
    print(shuru)

print('好好玩游戏...')