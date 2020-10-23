def max(*args):
    # 针对于参数的第一项是列表的时候
    if type(args[0]) == list:
        rMax = args[0][0]
    else:
        rMax = args[0]
    for i in args:
        # 其中一项是列表的情况,取出该列表的最大值和其他普通的数字参数作比较
        if type(i) == list:
            for y in i:
                if rMax < y:
                    rMax = y
        else: # 不是列表的时候
            if rMax < i:
                rMax = i
    return rMax
# print(max(234,23,43,534,5,45,4))
print(max([123,12,321,3,21321,222222222],234,23,43,[123,213,234,23,423,423,111111],534,[123,213,234,23,423,423,4444],5,45,4))

# a = [123,213,2,423]
# max = a[0]
# for i in a:
#     if max < i:
#         max = i
# print(max)