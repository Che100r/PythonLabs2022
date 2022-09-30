def func():
    return tuple([_ for _ in input().split() if int(_) % 2 == 0])


print(func())