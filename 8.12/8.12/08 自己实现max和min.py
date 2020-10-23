def max(*args):
    first = args[0]
    # 看args的第0项是什么类型
    if type(first) == list:
        # 相当于将该列表从大到小排序
        first.sort(reverse = True)
        return first[0]
    else:
        # 将args转化为列表
        args = list(args)
        # 列表就可以排序
        args.sort(reverse=True)
        return args[0]


print(max(10,20,30,345,345,2,3412,321))

print(max([102,325435,345,43]))