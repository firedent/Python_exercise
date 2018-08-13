# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint
from math import gcd, sqrt
import time

try:
    # arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
    arg_for_seed, length, max_value = 1, 1000, 10000
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []
start = time.time()

# REPLACE THIS COMMENT WITH YOUR CODE

# def prime_factors():
#     i = 2
#     while (1):
#         j = 2
#         while (j < i):
#             if (i % j == 0):
#                 break
#             j = j + 1
#         if (j == i):
#             yield i
#         i += 1


def prime_number_up_to(n):
    l = [True] * (n+1)
    pf = []
    for i in range(2, round(sqrt(n))+1):
        if l[i]:
            for j in range(i*i, n+1, i):
                l[j] = False
    for i in range(2, n+1):
        if l[i]:
            pf.append(i)
    return pf


def ob_prime_number_up_to(n):
    index = (n-1)//2
    l = [True] * (index + 1)
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
            while a % su == 0:
                a = a / su
                L.append(su)
            if a == 1:
                break
        if len(L) != 0:
            L_L.append(L)
    return L_L


def resolve_simple(n):
    l = []
    if n == 1:
        return []
    for i in pf:
        if n == 1:
            break
        while n%i == 0:
            l.append(i)
            n = n/i
    return l


def count_prime_factors(l):
    d = dict()
    for i in l:
        d[i] = d.get(i, 0) + 1
    return d


# pf = []
# for i in prime_factors():
#     if i > max_value:
#         break
#     pf.append(i)
pf = ob_prime_number_up_to(max_value)

# def get_dic_of_fraction(L):
#     dic_of_fraction = dict()
#     for i in L:
#         for j in L:
#             a, b = i, j
#             if a == b:
#                 dic_of_fraction[(1, 1)] = 1
#                 continue
#             if a > b:
#                 a, b = b, a
#             g = gcd(a, b)
#             a, b = int(a / g), int(b / g)
#             dic_of_fraction[(a, b)] = a / b
#     return dic_of_fraction
# dic_of_fraction = get_dic_of_fraction(L)


def get_dic_of_fraction(L):
    dic_of_fraction = dict()
    head = 0
    for i in L:
        for j in L[head:]:
            if i == j:
                dic_of_fraction[(1, 1)] = (2, 1)
                continue
            g = gcd(i, j)
            a, b = int(i / g), int(j / g)
            dic_of_fraction[(a, b)] = (len(str(a)+str(b)), i / j)
        head += 1
    return dic_of_fraction


L_ss = list(set(L))
L_ss.sort()
dic_of_fraction = get_dic_of_fraction(L_ss)

list_of_fraction_sorted = sorted(dic_of_fraction.items(), key=lambda a: (a[1][0], a[1][1]), reverse=False)

size_of_simplest_fraction = list_of_fraction_sorted[0][1][0]
size_of_most_complex_fraction = list_of_fraction_sorted[-1][1][0]

for i in list_of_fraction_sorted:
    if i[1][0] == size_of_simplest_fraction:
        simplest_fractions.append(i[0])
    else:
        break

set_of_denom = set()
dict_of_pf = dict()
for i in list_of_fraction_sorted[::-1]:
    if i[1][0] == size_of_most_complex_fraction:
        most_complex_fractions.append((i[0][0], i[0][1]))
        if i[0][1] not in set_of_denom:
            set_of_denom.add(i[0][1])
            dict_of_pf_denom = dict()
            for i in resolve_simple(i[0][1]):
                dict_of_pf_denom[i] = dict_of_pf_denom.setdefault(i, 0) + 1
            for i in dict_of_pf_denom.items():
                if i[1] > dict_of_pf.setdefault(i[0],0):
                    dict_of_pf[i[0]] = i[1]
    else:
        break

dict_of_pf_sorted = sorted(dict_of_pf.items(),key=lambda i: i[1])

if len(dict_of_pf_sorted) != 0:
    multiplicity_of_largest_prime_factor = dict_of_pf_sorted[-1][1]
    for i in dict_of_pf_sorted[::-1]:
        if i[1] == multiplicity_of_largest_prime_factor:
            largest_prime_factors.append(i[0])
        else:
            break
    largest_prime_factors.reverse()

print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
      )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
      )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
      )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
stop = time.time()
print(stop-start)
