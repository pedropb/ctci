"""
Magic Index: A magic index in an array A[ 1.•.n-1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
"""


def magic_index(arr) -> int:
  if len(arr) == 0:
    return None

  return find_magic_index(arr, 0, len(arr) - 1)

def find_magic_index(arr, start: int, end: int) -> int:
  if end < start:
    return -1

  mid_index = (start + end) // 2
  mid_value = arr[mid_index]
  if mid_index == mid_value:
    return mid_index

  # search left
  left_index = min(mid_index - 1, mid_value)
  left = find_magic_index(arr, start, left_index)
  if left >= 0:
    return left

  # search right
  right_index = max(mid_index + 1, mid_value)
  right = find_magic_index(arr, right_index, end)
  return right


print(magic_index([0]))
print(magic_index([1]))
print(magic_index([-4,-3,2,6,10]))
print(magic_index([-4,-3,-1,2,3,5,10]))
print(magic_index([4,4,4,4,10,10,10,10,10,10,10]))

