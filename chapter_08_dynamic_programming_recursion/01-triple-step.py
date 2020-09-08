"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
"""

def count_ways(number_of_steps, memo) -> int:
  if number_of_steps == 0:
    return 1
  elif number_of_steps < 0:
    return 0
  elif number_of_steps in memo:
    return memo[number_of_steps]
  else:
    memo[number_of_steps] = (count_ways(number_of_steps - 1, memo) +
      count_ways(number_of_steps - 2, memo) +
      count_ways(number_of_steps - 3, memo))
    return memo[number_of_steps]

print(count_ways(1, {}))
print(count_ways(2, {}))
print(count_ways(3, {}))
print(count_ways(10, {}))
