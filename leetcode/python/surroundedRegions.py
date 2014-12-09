# https://oj.leetcode.com/problems/surrounded-regions/

class Solution:
  # @param board, a 2D array
  # Capture all regions by modifying the input board in-place.
  # Do not return any value.
  def solve(self, board):
    if len(board) <= 2 or len(board[0]) <= 2:
      return

    for i in xrange(len(board)):
      board[i] = [c for c in board[i]]

    m, n = len(board), len(board[0])
    for j in xrange(n-1):
      self.markOpenRegions(board, 0, j, m, n)
    for i in xrange(m-1):
      self.markOpenRegions(board, i, n-1, m, n)
    for j in xrange(n-1):
      self.markOpenRegions(board, m-1, n-1-j, m, n)
    for i in xrange(m-1):
      self.markOpenRegions(board, m-1-i, 0, m, n)

    for i in xrange(m):
      for j in xrange(n):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'B':
          board[i][j] = 'O'

    for i in xrange(len(board)):
      board[i] = ''.join(board[i])

  # DFS recursion (Runtime Error at OJ)
  # def markOpenRegions(self, board, i, j, m, n):
  #   if not self.onBoard(i, j, m, n) or board[i][j] != 'O':
  #     return
  #   board[i][j] = 'B'
  #   for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
  #     self.markOpenRegions(board, i+d[0], j+d[1], m, n)

  def markOpenRegions(self, board, i, j, m, n):
    if not self.onBoard(i, j, m, n) or board[i][j] != 'O':
      return
    deltas, queue = [(-1, 0), (1, 0), (0, -1), (0, 1)], [(i,j)]
    while len(queue) > 0:
      pos = queue.pop()
      board[pos[0]][pos[1]] = 'B'
      for d in deltas:
        newPos = (pos[0]+d[0], pos[1]+d[1])
        if self.onBoard(newPos[0], newPos[1], m, n) and board[newPos[0]][newPos[1]] == 'O':
          queue.append(newPos)

  def onBoard(self, i, j, m, n):
    if i < 0 or j < 0 or i >= m or j >= n:
      return False
    return True

s = Solution()

board = ['XXXX','XOOX','XXOX','XOXX']
s.solve(board)
print board

board = ['OX']
s.solve(board)
print board

board = ['O','X']
s.solve(board)
print board

board = ["OOO","OOO","OOO"]
s.solve(board)
print board
