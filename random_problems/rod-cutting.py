"""
Rod cutting problem: Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the locations where the cuts are to be made for maximum profit
"""

calls = 0
def max_revenue(rod_size, price_table, memo):
  global calls
  if rod_size in memo:
    return memo[rod_size]

  calls +=1
  if rod_size == 0:
    return 0

  max_value = 0
  for i in range(1, rod_size + 1):
    max_value = max(max_value, price_table[i-1] + max_revenue(rod_size-i, price_table, memo))

  memo[rod_size] = max_value
  return memo[rod_size]

calls = 0
print(max_revenue(1, [1], {}))
print(f"calls: {calls}")
calls = 0
print(max_revenue(2, [1,10], {}))
print(f"calls: {calls}")
calls = 0
print(max_revenue(5, [1,2,4,5,10], {}))
print(f"calls: {calls}")

