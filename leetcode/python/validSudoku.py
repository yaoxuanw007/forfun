# https://oj.leetcode.com/problems/valid-sudoku/

class Solution:
  # @param board, a 9x9 2D array
  # @return a boolean
  def isValidSudoku(self, board):

    # 1*9
    for r in xrange(9):
      record = 0
      for c in xrange(9):
        record = self.setRecord(record, board[r][c])
        if record < 0:
          return False

    # 9*1
    for c in xrange(9):
      record = 0
      for r in xrange(9):
        record = self.setRecord(record, board[r][c])
        if record < 0:
          return False

    # 3*3
    for i in xrange(3):
      for j in xrange(3):
        record = 0
        for k in xrange(3):
          for l in xrange(3):
            r, c = i * 3 + k, j * 3 + l
            record = self.setRecord(record, board[r][c])
            if record < 0:
              return False

    return True

  def setRecord(self, record, num):
    if num == '.':
      return record
    x = 1 << int(num)
    if record & x:
      return -1
    return record | x

s = Solution()

print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
