# https://oj.leetcode.com/problems/set-matrix-zeroes/

class Solution:
  # @param matrix, a list of lists of integers
  # RETURN NOTHING, MODIFY matrix IN PLACE.
  def setZeroes(self, matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return
    m, n = len(matrix), len(matrix[0])
    hasFirstZero = False
    for j in xrange(n):
      if matrix[0][j] == 0 and not hasFirstZero:
        hasFirstZero = True
        break
    for i in xrange(1, m):
      hasZero = False
      for j in xrange(n):
        if matrix[i][j] == 0:
          if not hasZero:
            hasZero = True
          matrix[0][j] = 0
      # set zero in row
      if hasZero:
        for j in xrange(n):
          matrix[i][j] = 0
    # set zero in all columns
    for j in xrange(n):
      if matrix[0][j] == 0:
        for i in xrange(m):
          matrix[i][j] = 0
    # set first row
    if hasFirstZero:
      for j in xrange(n):
        matrix[0][j] = 0

s = Solution()

matrix = [[0,1],[1,1]]
s.setZeroes(matrix)
print matrix
