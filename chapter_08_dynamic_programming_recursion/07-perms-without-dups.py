"""
Permutations without Dups: Write a method to compute all permutations of a string of unique characters
"""
from typing import List

# ABC -> ABC, ACB, BAC, BCA, CAB, CBA O(n!)
# A -> A
# AB -> AB, BA
# N -> N * n-1 * n-2 * n-3 ... * 1

def permutations(string) -> List[str]:
  if len(string) == 1:
    return string

  perms = []
  for i, c in enumerate(string):
    perms += [c + p for p in permutations(string[:i] + string[i+1:])]

  return perms

print(permutations('a'))
print(permutations('ab'))
print(permutations('abc'))
print(permutations('abcd'))
