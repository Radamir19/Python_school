result = []
for A in range(100):
    flag = 1
    for x in range(100):
        for y in range(100):
            f = (75 != 2 * x + 3 * y) or (A > 3 * x) or (A > 2 * y)
            if f == 0:
                flag = 0
    if flag == 1:
        result.append(A)

print(min(result))