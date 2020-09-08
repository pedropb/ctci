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
