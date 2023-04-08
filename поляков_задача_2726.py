def to_3 (x):
    res = ''
    while x:
        res += str(x % 3)
        x //= 3
    return res[::-1]

a = to_3((2 ** 5 * 3 ** 25))
print(a.count('0'))