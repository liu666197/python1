import sys
# 设置递归深度
sys.setrecursionlimit(5000)
count = 0
def f(count):
    count += 1
    print('hello', count)
    if count == 10:
        return None

    f(count)

f(count)