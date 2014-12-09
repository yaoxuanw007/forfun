# https://oj.leetcode.com/problems/spiral-matrix-ii/

class Solution:
  # @return a list of lists of integer
  def generateMatrix(self, n):
    matrix = [[0]*n for i in xrange(n)]
    next = 1
    for k in xrange(n/2):
      for j in xrange(k, n-1-k):
        matrix[k][j] = next
        next += 1
      for i in xrange(k, n-1-k):
        matrix[i][n-1-k] = next
        next += 1
      for j in xrange(k, n-1-k):
        matrix[n-1-k][n-1-j] = next
        next += 1
      for i in xrange(k, n-1-k):
        matrix[n-1-i][k] = next
        next += 1
    if n % 2 == 1:
      matrix[n/2][n/2] = next
    return matrix

s = Solution()

print s.generateMatrix(1)
print s.generateMatrix(2)
print s.generateMatrix(3)
