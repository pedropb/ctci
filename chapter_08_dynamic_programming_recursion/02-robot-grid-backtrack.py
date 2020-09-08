from typing import List

board = [
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [0, 0, 1, 0, 1],
  [0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1],
]

Board = List[List[int]]

class Point:

  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __eq__(self, other):
    return self.row == other.row and self.col == other.col

  def move_right(self):
    return Point(self.row, self.col + 1)

  def move_down(self):
    return Point(self.row + 1, self.col)

  def __str__(self):
    return f"({self.row}, {self.col})"

  def __hash__(self):
    return hash((self.row, self.col))

EXIT = Point(len(board)-1, len(board[0])-1)

class Board:
  def __init__(self, data: Board):
    self.data = data

  def is_valid(self, position: Point):
    return position.row < len(self.data) and position.col < len(self.data[0]) and self.data[position.row][position.col] == 1



BOARD_EXIT = Point(len(board) - 1, len(board[0]) - 1)

calls = 0

def solver_brute(board: Board) -> List[Point]:
  start = Point(row=0, col=0)
  path = []
  memo = {}
  if find_exit(board, path, start, memo):
    print('\n'.join([str(p) for p in path]))
    print(f"Calls: {calls}")
  else:
    print('Did not find a path')

calls = 0

def find_exit(board, path, current: Point, memo) -> bool:
  global calls
  calls += 1

  path.append(current)
  if current == BOARD_EXIT:
    return True

  if current in memo:
    return memo[current]


  if board.is_valid(current.move_right()):
    if find_exit(board, path, current.move_right(), memo):
      # we found the exit by moving right
      return True
    else:
      path.pop()

  # we didn't find the exit moving right,
  # so we backtrack and try moving down
  if board.is_valid(current.move_down()):
    if find_exit(board, path, current.move_down(), memo):
      # we found the exit by moving down
      return True
    else:
      path.pop()

  # we didn't find the exit moving down either,
  # so we back track and try again in a different
  # branch
  memo[current] = False
  return False

solver_brute(Board(board))





