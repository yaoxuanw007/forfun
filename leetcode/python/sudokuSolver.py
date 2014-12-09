# https://oj.leetcode.com/problems/sudoku-solver/

class Solution:
  # @param board, a 9x9 2D array
  # Solve the Sudoku by modifying the input board in-place.
  # Do not return any value.
  def solveSudoku(self, board):
    if len(board) == 0 or len(board[0]) == 0:
      return
    m, n = len(board), len(board[0])
    for i in xrange(m):
      board[i] = [x for x in board[i]]
    self.solve(board, m, n)
    for i in xrange(m):
      board[i] = ''.join(board[i])

  def solve(self, board, m, n):
    for i in xrange(m):
      for j in xrange(n):
        if board[i][j] == '.':
          for k in xrange(1, 10):
            board[i][j] = str(k)
            if self.isValid(board, i, j) and self.solve(board, m, n):
              return True
            board[i][j] = '.'
          return False
    return True

  def isValid(self, board, x, y):
    # 1*9
    flags = [False] * 9
    for i in xrange(9):
      if board[x][i] != '.':
        num = int(board[x][i]) - 1
        if flags[num]:
          return False
        flags[num] = True
    # 9*1
    flags = [False] * 9
    for i in xrange(9):
      if board[i][y] != '.':
        num = int(board[i][y]) - 1
        if flags[num]:
          return False
        flags[num] = True
    # 3*3
    flags = [False] * 9
    r, c = x/3, y/3
    for i in xrange(3):
      for j in xrange(3):
        if board[r*3+i][c*3+j] != '.':
          num = int(board[r*3+i][c*3+j]) - 1
          if flags[num]:
            return False
          flags[num] = True
    return True

import pprint as pp

# Pass OJ !!
class Solution1:
  # @param board, a 9x9 2D array
  # Solve the Sudoku by modifying the input board in-place.
  # Do not return any value.
  def solveSudoku(self, board):
    if len(board) == 0 or len(board[0]) == 0:
      return
    m, n = len(board), len(board[0])
    for i in xrange(m):
      board[i] = [x for x in board[i]]
    self.createBoardAvail(board, m, n)
    self.solve(board, m, n)
    for i in xrange(m):
      board[i] = ''.join(board[i])

  def createBoardAvail(self, board, m, n):
    self.boardAvail = [[None]*n for i in xrange(m)]
    for x in xrange(m):
      for y in xrange(n):
        self.boardAvail[x][y] = set([str(k) for k in range(1,10)])
    for x in xrange(m):
      for y in xrange(n):
        self.removeBoardAvail(board, x, y)
    # pp.pprint(self.boardAvail)

  def removeBoardAvail(self, board, x, y, boardDelta=None):
    if board[x][y] != '.':
      for i in xrange(9):
        if board[x][y] in self.boardAvail[i][y]:
          if boardDelta:
            boardDelta[i][y] = True
          self.boardAvail[i][y].remove(board[x][y])
      for i in xrange(9):
        if board[x][y] in self.boardAvail[x][i]:
          if boardDelta:
            boardDelta[x][i] = True
          self.boardAvail[x][i].remove(board[x][y])
      r, c = x//3, y//3
      for i in xrange(3):
        for j in xrange(3):
          if board[x][y] in self.boardAvail[r*3+i][c*3+j]:
            if boardDelta:
              boardDelta[r*3+i][c*3+j] = True
            self.boardAvail[r*3+i][c*3+j].remove(board[x][y])

  def addBoardAvail(self, board, x, y, boardDelta):
    if board[x][y] != '.':
      for i in xrange(9):
        for j in xrange(9):
          if boardDelta[i][j]:
            boardDelta[i][j] = False
            self.boardAvail[i][j].add(board[x][y])

  def solve(self, board, m, n):
    for x in xrange(m):
      for y in xrange(n):
        if board[x][y] == '.':
          boardDelta = [[False]*n for i in xrange(m)]
          for num in [str(n) for n in xrange(1, 10)]:
            if num in self.boardAvail[x][y]:
              board[x][y] = num
              self.removeBoardAvail(board, x, y, boardDelta)
              # pp.pprint([board, self.boardAvail])
              if self.solve(board, m, n):
                return True
              self.addBoardAvail(board, x, y, boardDelta)
              board[x][y] = '.'
          return False
    return True

# Test

s = Solution1()

board = [".87654329","2........","3........","4........","5........","6........","7........","8........","9........"]
s.solveSudoku(board)
print board

