
# 1-100的和

def f(n):
    if n == 1:
        return 1
    # f(100)  return 100 + f(99)
    # f(99)  return 99 + f(98)
    # f(98)  return 98 + f(97)
    # ..
    # f(2)  return 2 + 1
    # f(1)  return 1
    return n + f(n - 1)

print(f(1000))
