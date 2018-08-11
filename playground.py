from math import gcd, sqrt
def ob_prime_number_up_to(n):
    index = (n-1)//2
    l = [True] * (index + 1)
    if n < 2:
        return []
    pf = [2]
    for i in range(1, (round(sqrt(n))+1)//2):
        if l[i]:
            for j in range(2*i*(i+1), index+1, 2*i+1):
                l[j] = False
    for i in range(1, index+1):
        if l[i]:
            pf.append(2*i+1)
    return pf

def resolve(ll):
    L_L = []
    for a in ll:
        L = []
        for su in pf:
            while (a % su == 0):
                a = a / su
                L.append(su)
            if a == 1:
                break
        if len(L) != 0:
            L_L.append(L)
    return L_L

print(ob_prime_number_up_to(1000))