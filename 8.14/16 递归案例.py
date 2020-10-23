# 设计一个递归函数,功能: 求n的阶乘
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)
print(f(5))

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return f(n - 1) + f(n - 2)
print(f(24))

def monkey(n):
    if n == 7:
        return 1
    return (monkey(n + 1) + 1) * 2
print(monkey(1))