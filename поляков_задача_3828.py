def DEL(n, m):
    return n % m == 0

result = []
for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        f = DEL(A, 12) and (DEL(530, x) <= ((not DEL(A, x)) <= (not DEL(170, x))))
        if f == 0:
            flag = 0
    if flag == 1:
        result.append(A)

print(min(result))