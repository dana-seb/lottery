import numpy as np
import pandas as pd
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import product
print('\n')

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# prints the combinations from 3 digits with the numbers from 0-9
comb = combinations(number, 3)
my_comb = []
for i in list(comb):
    # print(i)
    my_comb.append(i)
# print(my_comb)
# print(len(my_comb))

# Combinations with replacements for 3 digit with numbers ranging from 0-9
comb = combinations_with_replacement(number, 3)
my_comb_replace = []
for i in list(comb):
    # print(i)
    my_comb_replace.append(i)
# print(my_comb)
# print(len(my_comb))

# Permutations of a list from 0-9; 3 digit number
""" perm = permutations(number, 3)
my_perm = []
for i in list(perm):
    # print(i)
    my_perm.append(i) """
# print(my_perm)
# print(len(my_perm))

""" my_list = [(5, 9, 0)]
df = pd.DataFrame(my_list)
print(df) """

df_comb = pd.DataFrame(my_comb)
df_comb_rep = pd.DataFrame(my_comb_replace)
# df_perm = pd.DataFrame(my_perm)

# print(df_perm)

""" df_comb.to_excel('va_lottery_comb.xlsx', sheet_name='combo')
df_comb_rep.to_excel('va_lottery_crep.xlsx', sheet_name='combo_rep')
df_perm.to_excel('va_lottery_perm.xlsx', sheet_name='perm') """

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
my_perm = []
for i in list(perm):
    # print(i)
    my_perm.append(i)
# print(my_perm)
# print(len(my_perm))

""" p1 = product("2357", repeat=3)
y = [*map(''.join, p1)]
print(y) """

""" p1 = product("0123456789", repeat=3)
y = [*map(''.join, p1)]
print(y)
print(len(y)) """

p1 = product("003", repeat=3)
y = [*map(''.join, p1)]
# print(y)
# print(len(y))

v = np.unique_counts(y)
print(v)

print('\n')