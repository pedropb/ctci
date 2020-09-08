"""
Power Set: Write a method to return all subsets of a set
"""

# s12 = set([1, 2])
# ps12 = [], [1], [2], [1, 2]
# s123 = set([1, 2, 3])
# power_set = [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
# ps123 - ps12 = [3], [1, 3], [2, 3], [1, 2, 3]
# ps123 = ([3] * ps12) + ps12
# pn = n * pn-1 + pn-1

from itertools import chain, combinations

def power_set_pythonic(initial_set):
  return [*chain.from_iterable(combinations(initial_set, i) for i in range(len(initial_set) + 1))]

print(power_set_pythonic([1,2,3]))

def power_set_combinatorics(initial_set):
  size = len(initial_set)

  power_sets = []
  # for each combination of element in/out of subset
  for i in range(1 << size):
    # add combination to power_set
    power_sets.append([initial_set[j] for j in range(size) if i & (1 << j)])

  return power_sets

print(power_set_combinatorics([]))
print(power_set_combinatorics([1,2,3]))
print(power_set_combinatorics([1,2,3,4]))



