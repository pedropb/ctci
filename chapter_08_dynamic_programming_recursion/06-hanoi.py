"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.
"""

from __future__ import annotations

# Top --> Bottom
# 1, 2     0, 0     0, 0
# 0, 2     0, 1     0, 0
# 0, 0     0, 1     0, 2
# 0, 0     0, 0     1, 2

# 1, 2, 3     0, 0, 0    0, 0, 0
# 0, 2, 3     0, 0, 0    0, 0, 1
# 0, 0, 3     0, 0, 2    0, 0, 1
# 0, 0, 3     0, 1, 2    0, 0, 0
# 0, 0, 0     0, 1, 2    0, 0, 3
# 0, 0, 1     0, 0, 2    0, 0, 3
# 0, 0, 1     0, 0, 0    0, 2, 3
# 0, 0, 0     0, 0, 0    1, 2, 3

# 1, 2, 3, 4     0, 0, 0, 0    0, 0, 0, 0
# 0, 2, 3, 4     0, 0, 0, 1    0, 0, 0, 0
# 0, 0, 3, 4     0, 0, 0, 1    0, 0, 0, 2
# 0, 0, 3, 4     0, 0, 0, 0    0, 0, 1, 2
# 0, 0, 0, 4     0, 0, 0, 3    0, 0, 1, 2
# 0, 0, 1, 4     0, 0, 0, 3    0, 0, 0, 2
# 0, 0, 1, 4     0, 0, 2, 3    0, 0, 0, 0
# 0, 0, 0, 4     0, 1, 2, 3    0, 0, 0, 0
# 0, 0, 0, 0     0, 1, 2, 3    0, 0, 0, 4
# 0, 0, 0, 0     0, 0, 2, 3    0, 0, 1, 4
# 0, 0, 0, 2     0, 0, 0, 3    0, 0, 1, 4
# 0, 0, 1, 2     0, 0, 0, 3    0, 0, 0, 4
# 0, 0, 1, 2     0, 0, 0, 0    0, 0, 3, 4
# 0, 0, 1, 2     0, 0, 0, 0    1, 2, 3, 4

class Tower:
  def __init__(self, index: int):
    self.disks = []
    self.index = index

  def moveTopDisk(self, other: Tower):
    disk = self.disks.pop()
    print(f"Moving disk {disk} from tower {self.index} to tower {other.index}")
    other.receiveDisk(disk)

  def receiveDisk(self, disk: int):
    if len(self.disks) > 0 and self.disks[-1] < disk:
      raise Exception("Disk is bigger than the disk at the top of the tower")
    self.disks.append(disk)

  def moveDisks(self, number_of_disks: int, destination: Tower, buffer: Tower):
    if number_of_disks > 0:
      self.moveDisks(number_of_disks-1, buffer, destination)
      self.moveTopDisk(destination)
      buffer.moveDisks(number_of_disks-1, destination, self)

def hanoi_solver(number_of_disks):
  print(f"Hanoi Solver with {number_of_disks} disks")
  print("----------------------------------------")
  towers = [Tower(i) for i in range(1, 4)]
  for disk in range(number_of_disks, 0, -1):
    towers[0].receiveDisk(disk)

  towers[0].moveDisks(number_of_disks, towers[2], towers[1])
  print("----------------------------------------")
  print()


hanoi_solver(2)
hanoi_solver(3)
hanoi_solver(4)
hanoi_solver(5)





