result = []
for A in range(100):
    flag = 1
    for x in range(100):
        f = (((x & 13 != 0) or (x & 39 == 0)) <= (x & 13 != 0)) or ((x & A == 0) and (x & 13 == 0))
        if f == 0:
            flag = 0
    if flag == 1:
        result.append(A)

print(max(result))