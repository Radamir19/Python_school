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
# print(resolve(30, 12) * resolve(12, 1)).


