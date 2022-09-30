from statistics import mean


def inp():
    return mean([int(_) for _ in input().split()])


print(inp())
