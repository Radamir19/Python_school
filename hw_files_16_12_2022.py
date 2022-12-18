# a = [i for i in open('17.txt')]
# s = []
# for i in range(len(a) - 1):
#     x = int(a[i])
#     y = int(a[i + 1])
#     if 50 <= abs(x) + abs(y) <= 200:
#         s.append(abs(x) + abs(y))
# print(len(s), min(s))

# a = [i for i in open('17_1.txt')]
# s = []
# for i in range(len(a) - 2):
#     x = a[i]
#     y = a[i + 1]
#     z = a[i + 2]
#     if x[-1:] != '3' and y[-1:] != '3' and z[1:] != '3':
#         s.append(int(x) + int(y) + int(z))
# print(len(s), min(s))

a = [int(i) for i in open('17_1.txt')]
s = [x for x in range(len(a) - 2) if str(a[x])[-1:] != '3' and str(a[x + 1])[-1:] != '3' and str(a[x + 2])[-1:] != '3' (a[x] + a[x + 1] + a[x + 2])]
print(len(s), min(sum(s)))