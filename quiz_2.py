# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint
from math import gcd
import time

try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
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


# REPLACE THIS COMMENT WITH YOUR CODE

start = time.time()
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

pf = []
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


def sort_fraction(x):
    return x[2], x[1]


def count_prime_factors(l):
    d = dict()
    for i in l:
        d[i] = d.get(i, 0) + 1
    return d

for i in prime_factors():
    if i > max_value:
        break
    pf.append(i)


def get_dic_of_fraction(L):
    dic_of_fraction = dict()
    for i in L:
        for j in L:
            a, b = i, j
            if a > b:
                a, b = b, a
            # more time
            # if (a, b) not in dic_of_gcd:
            #     g = dic_of_gcd[(a, b)] = gcd(a, b)
            # else:
            #     g = dic_of_gcd[(a, b)]
            g = gcd(a, b)
            a, b = int(a / g), int(b / g)
            if a == b:
                dic_of_fraction[(a, b)] = 1
                continue

            dic_of_fraction[(a, b)] = a / b
    return dic_of_fraction
dic_of_fraction = get_dic_of_fraction(L)


list_of_fraction = []
for x in dic_of_fraction.items():
    size = 0
    for i in x[0]:
        size += len(str(i))
    list_of_fraction.append((x[0], x[1], size))

list_of_fraction_sorted = sorted(list_of_fraction, key=sort_fraction)

size_of_simplest_fraction = list_of_fraction_sorted[0][2]
size_of_most_complex_fraction = list_of_fraction_sorted[-1][2]
for i in list_of_fraction_sorted:
    if i[2] == size_of_simplest_fraction:
        simplest_fractions.append(i[0])
    else:
        break
for i in reversed(list_of_fraction_sorted):
    if i[2] == size_of_most_complex_fraction:
        most_complex_fractions.append(i[0])
    else:
        break

set_of_denominators = set()
dic_of_multiplicity_of_PF = dict()
for i in most_complex_fractions:
    set_of_denominators.add(i[1])

list_of_NB_of_PF_denominators = []
for i in list(resolve(set_of_denominators)):
    for j in count_prime_factors(i).items():
        pf = j[0]
        multi = j[1]
        if multi > dic_of_multiplicity_of_PF.get(pf, 0):
            dic_of_multiplicity_of_PF[pf] = multi


dic_of_multiplicity_of_PF_sorted = sorted(dic_of_multiplicity_of_PF.items(), key=lambda x: x[1], reverse=True)

if len(dic_of_multiplicity_of_PF_sorted) != 0:
    multiplicity_of_largest_prime_factor = dic_of_multiplicity_of_PF_sorted[0][1]
    for i in dic_of_multiplicity_of_PF_sorted:
        if i[1] == multiplicity_of_largest_prime_factor:
            largest_prime_factors.append(i[0])
        else:
            break

largest_prime_factors.sort()

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
