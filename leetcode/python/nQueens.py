# https://oj.leetcode.com/problems/n-queens/

class Solution:
  # @return a list of lists of string
  def solveNQueens(self, n):
    result, board = [], [0] * n
    self.dfs(board, 0, result)
    for i in xrange(len(result)):
      result[i] = self.convertBoard(result[i])
    return result

  def convertBoard(self, board):
    n = len(board)
    for i in xrange(n):
      num, board[i] = board[i], ""
      for j in xrange(n):
        if num & 1 != 0:
          board[i] += 'Q'
        else:
          board[i] += '.'
        num >>= 1
    return board

  def noAttack(self, board, x, y):
    n = len(board)
    # row
    if board[x] != 0:
      return False
    # col
    for i in xrange(n):
      if board[i] & (1<<y) != 0:
        return False
    deltas = [(-1,-1),(1,1),(-1,1),(1,-1)]
    for d in deltas:
      newX, newY = x, y
      while newX >= 0 and newX < n and newY >= 0 and newY < n:
        if board[newX] & (1<<newY) != 0:
          return False
        newX += d[0]
        newY += d[1]
    return True

  def dfs(self, board, x, result):
    n = len(board)
    if x == n:
      result.append(board[:])
      return
    for y in xrange(n):
      if self.noAttack(board, x, y):
        board[x] |= 1<<y
        self.dfs(board, x+1, result)
        board[x] = 0

s = Solution()

print s.solveNQueens(4)
