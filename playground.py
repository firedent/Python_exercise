# coding=utf-8
def prime_factors():
    i = 2
    while (1):
        j = 2
        while (j < i):
            if (i % j == 0):
                break
            j = j + 1
        if (j == i):
            yield i
        i += 1


def resolve(ll):
    L_L = []
    for a in ll:
        L = []
        for su in prime_factors():
            a, b = divmod(a, su)
            while (b == 0):
                L.append(su)
                a, b = divmod(a, su)
                if (a == 1):
                    break

        if len(L) != 0:
            L_L.append(L)
    return L_L


l = []
for i in prime_factors():
    if i > 10000:
        break
    l.append(i)