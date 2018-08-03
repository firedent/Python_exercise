# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

# REPLACE THIS COMMENT WITH YOUR CODE

distinct_digits = [0] * 9
L_resolved = []
d = dict()
l_of_gap = []
num_of_ele_in_dict = 0


def resolve(e):
    if e == 0:
        return [0]
    l = []
    a, b = e, 0
    while a != 0:
        a, b = divmod(a, 10)
        l.append(b)
    l.reverse()
    return l


sum_of_digits_in_x = sum(resolve(x))

for i in L:
    num_of_ele = len(set(resolve(i)))
    distinct_digits[num_of_ele] = distinct_digits[num_of_ele] + 1
    L_resolved.append(resolve(i))

for i in L_resolved:
    if i[0] > i[-1]:
        first_digit_greater_than_last += 1
    elif i[0] == i[-1]:
        same_first_and_last_digits += 1
    else:
        last_digit_greater_than_first += 1

    l_of_gap.append(abs(i[0] - i[-1]))

    d[(i[0], i[-1])] = d.get((i[0], i[-1]), 0) + 1

l_of_gap.sort()
min_gap = l_of_gap[0]
max_gap = l_of_gap[-1]

l_of_dict = sorted(d.items(), key=lambda a: a[1], reverse=True)
for i in l_of_dict:
    if i[1] < num_of_ele_in_dict:
        break
    first_and_last.add(i[0])
    num_of_ele_in_dict = i[1]

print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
      )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
      )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
      )
