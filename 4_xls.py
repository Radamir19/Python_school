a = [[int(i) for i in x.split()] for x in open('4.txt.txt')]
pov = []
nepov = []
k = 0
for stroka in a:
    m_in_sqrt = 0
    m_ax_sqrt = 0
    s = 0
    if len(set(stroka)) <= 6:
        for i in stroka:
            if stroka.count(i) == 2: pov.append(i)
            elif stroka.count(i) == 3: pov.append(i)
            else: nepov.append(i)
        m_in_sqrt = min(stroka) * min(stroka)
        m_ax_sqrt = max(stroka) * max(stroka)
        for j in nepov:
            s += j * j
        if(s < (m_in_sqrt + m_ax_sqrt)):
            k += 1
print(k)

