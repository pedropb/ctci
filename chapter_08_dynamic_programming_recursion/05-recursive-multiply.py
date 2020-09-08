"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
"""

# recursive_multiply(5, 3) =  5 + recursive_multiply(5, 2)
# recursive_multiply(5, 2) = recursive_multiply(5, 1) >> 1
# recursive_multiply(5, 1) = 5


def recursive_multiply(op1, op2):
  bigger = max(op1, op2)
  smaller = min(op1, op2)

  if smaller == 0:
    return 0

  if smaller == 1:
    return bigger
  elif smaller % 2 == 1:
    return bigger + recursive_multiply(bigger, smaller-1)
  else:
    return recursive_multiply(bigger, smaller >> 1) << 1

print(recursive_multiply(5,3))
print(recursive_multiply(5,1))
print(recursive_multiply(3,0))
print(recursive_multiply(45,72))
