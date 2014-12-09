# https://oj.leetcode.com/problems/n-queens-ii/

class Solution:
  # @return an integer
  def totalNQueens(self, n):
    self.result, board = 0, [0] * n
    self.dfs(board, 0)
    return self.result

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

  def dfs(self, board, x):
    n = len(board)
    if x == n:
      self.result += 1
      return
    for y in xrange(n):
      if self.noAttack(board, x, y):
        board[x] |= 1<<y
        self.dfs(board, x+1)
        board[x] = 0

s = Solution()

print s.totalNQueens(4)
