def reverse(_):
    rev = list(reversed(_.split()))
    return rev


str1 = input()
a = reverse(str1)

print(' '.join(a))
