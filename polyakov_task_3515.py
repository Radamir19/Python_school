def to_7 (x):
    res = ''
    while x:
        res += str(x % 7)
        x //= 7
    return res[::-1]

a = to_7((43 * 7 ** 103 - 21 * 7 ** 57 + 98))
a = sum(map(int, a))
print(a)