def factorial_cifri(x_i):
    if x_i <= 1:
        return 1
    else:
        return x_i * factorial_cifri(x_i - 1)


def fact_chisla(x_i):
    s_i = 0
    if x_i <= 1:
        return 1
    else:
        for i in str(x_i):
            s_i += factorial_cifri(int(i))
        return s_i


a = [int(i) for i in open('17_5.txt')]


def sum_dig(n):
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


s1 = 0
for i in range(len(a)):
    m = sum_dig(a[i])
    s1 += m
s2 = 0
for i in str(s1):
    s2 += int(i)

couples_list = []
for i in range(len(a) - 1):
    x = fact_chisla(a[i])
    y = fact_chisla(a[i + 1])
    if (x % s2 == 0) ^ (y % s2 == 0):
        couples_list.append(x + y)
print(len(couples_list))