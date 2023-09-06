from random import randint
from time import time
# task 2
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (not(w <= z)) or (x <= y) or (not x)
#                 if f == 0:
#                     print(w, z, y, x)

# task 5
# for i in range(1000):
#     n = bin(i)[2:]
#     n1 = ''
#     if n.count('1') % 2 == 0:
#         n += '0'
#         n1 = '10' + n[3:]
#     else:
#         n += '1'
#         n1 = '11' + n[3:]
#     R = int(n1, 2)
#     if R >= 16:
#         print(i)

# task 6
# for i in range(1000):
#     s = i
#     s = (s - 21) // 10
#     n = 1
#     while s >= 0:
#         n *= 2
#         s -= n
#     if n == 8:
#         print(i)
#         break

# task 12
# s = '9' * 96
# while ('22222' in s) or ('9999' in s):
#     if ('22222' in s) :
#         s = s.replace('22222', '99', 1)
#     elif ('9999' in s) :
#         s = s.replace('9999', '2', 1)
# print(s)

# task 14
# def to_5(a):
#     res = ''
#     while a > 0:
#         res += str(a % 5)
#         a //= 5
#     return res[::-1]
#
# a = 4 * 625 ** 1920 + 4 * 125 ** 1930 - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
# result = to_5(a)
# print(result.count('0'))


# task 15
# def DEL(n, m):
#     return n % m == 0
#
# for A in range(1, 1000):
#     flag = 1
#     for x in range(1, 1000):
#         f = (DEL(x, 2) <= (not DEL(x, 3))) or ((x + A) >= 80)
#         if f == 0:
#             flag = 0
#     if flag == 1:
#         print(A)
#         break


# task 17
# a = [int(i) for i in open('17_4597.txt')]
# m = min(a)
# res = []
# for i in range(len(a) - 1):
#     f = a[i]
#     s = a[i + 1]
#     if ((f % 117 == m) or (s % 117 == m)) :
#         res.append((f + s))
# print(max(res))


# # task 22
# for i in range(1000):
#     x = i
#     q = 6
#     p = 10
#     k1 = 0
#     k2 = 0
#     while x <= 100:
#         k1 += 1
#         x += p
#     while x >= q:
#         k2 += 1
#         x -= q
#     l = x + k1
#     m = x + k2
#     if (l == 8 and m == 21) :
#         print(i)
#


# # task 23
# def resolve(x, y):
#     if x < y:
#         return 0
#     if x == y:
#         return 1
#     return resolve(x - 1, y) + resolve((x % 2), y)
#
# print(resolve(30, 12) * resolve(12, 1))


# task 4
# for i in range(1000):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n += '10'
#     else:
#         n += '11'
#     if n.count('1') % 2 == 0:
#         n += n[-1]
#     else:
#         n += n[-2]
#     R = int(n, 2)
#     if R > 44:
#         print(i)
#         break

# d = 1
# while d < 40:
#     p = 5
#     q = 7
#     e = 11
#     f_n = (p - 1) * (q - 1)
#     if (d * e) % f_n == 1:
#         print(d)
#     d += 1

# print((~18 | (132 >> 2)) & (86 << 1))


# def resolve(x, y):
#     if x > y or x == 32:
#         return 0
#     if x == y:
#         return 1
#     return resolve(x + 3, y) + resolve(x + 4, y) + resolve(x * 3, y)
#
# print(resolve(4, 16) * resolve(16, 46))

# k = 0
# for i in range(1000):
#     s = i
#     n = 120
#     while s > 0:
#         s //= 6
#         n -= 6
#     if i % 2 == 0 and n == 108:
#         k += 1
# print(k)

# a = [int(i) for i in open('13.txt')]
# res = []
# for i in range(len(a) - 1):
#     if (a[i] % 8 == 0 and a[i + 1] % 8 == 0):
#         res.append(a[i] + a[i + 1])
# print(len(res), min(res))

# N = int(input())
# K = int(input())
# P = int(input())
# U = int(input())
#
# d = abs(P - U)
# t = divmod(d, K)
# j = P % K if P > U < K else (N - P) % K if P < U > N - K else K
# print(min(sum(t), 1 + j + int.__sub__(*t)))


# from math import prod, isqrt
# a, r1, _ = sides = tuple(map(int, map(input, ('',) * 3)))
# p = sum(sides)
# sq = prod(map(int.__sub__, (p,) * 4, map((2).__mul__, (0,) + sides))) // (4 * a * a)
# print(isqrt(r1 * r1 - sq), -isqrt(sq), sep = '\n')

#
# N = int(input())
# K = int(input())
# p = []
# for i in range(1, N + 1):
#     p.append(i)
# st = 0
# isFound = False
# while len(p) > 0:
#     st += 1
#     if p[0] == K:
#         isFound = True
#         break
#     p.pop(0)
#     if p[0] == K:
#         isFound = False
#         st += 1
#         break
#     p.pop(0)
#     st += 1
#     p.append(p.pop(0))
#     st += 1
#     if len(p) % 2 == 0:
#         st += len(p)
#         break
#     else:
#         st += len(p) + 1
#         break



# n = int(input())
# k = int(input())
# p = []
# for i in range(1, n + 1):
#     p.append(i)
# st = 0
# isFound = False
# while len(p) > 0:
#     if p[0] == k:
#         isFound = True
#         st += 1
#         break
#     p.pop(0)
#     st += 1
#     if p[0] == k:
#         isFound = False
#         st += 1
#         break
#     p.pop(0)
#     st += 1
#     p.append(p.pop(0))
#     st += 1
# if isFound == True:
#     print("Yes")
#     print(st)
# else:
#     print("No")
#     print(st)

n = int(input())
k = 0
t1 = time()
for i in range(n):
    if i % 2 == 0:
        x = bin(i)[2:]
        if x.count('1') % 2 == 0:
            k += 1
t2 = time()
print(t2 - t1)
print(k)