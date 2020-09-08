from typing import List

board = [
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [0, 0, 1, 0, 1],
  [1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1],
]

Board = List[List[int]]

class Point:

  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __eq__(self, other):
    return self.row == other.row and self.col == other.col

  def move_left(self):
    return Point(self.row, self.col - 1)

  def move_up(self):
    return Point(self.row - 1, self.col)

  def __str__(self):
    return f"({self.row}, {self.col})"

  def __hash__(self):
    return hash((self.row, self.col))

class Board:
  def __init__(self, data: Board):
    self.data = data

  def is_valid(self, position: Point):
    return position.row >= 0 and position.col >= 0 and position.row < len(self.data) and position.col < len(self.data[0]) and self.data[position.row][position.col] == 1

BOARD_EXIT = Point(len(board) - 1, len(board[0]) - 1)
START = Point(0, 0)

calls = 0

def solver_dp():
  path = []
  if find_path(Board(board), path, BOARD_EXIT, {}):
    print(*path)
    print(f"calls: {calls}")


def find_path(board, path, current: Point, memo):
  global calls
  calls += 1
  if current == START:
    return True

  if current in memo:
    return memo[current]

  if not board.is_valid(current):
    memo[current] = False
    return memo[current]

  if find_path(board, path, current.move_left(), memo):
    path.append(current.move_left())
    return True

  if find_path(board, path, current.move_up(), memo):
    path.append(current.move_up())
    return True

  memo[current] = False
  return memo[current]


solver_dp()
