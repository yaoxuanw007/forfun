# https://oj.leetcode.com/problems/unique-paths/

class Solution:
  # @return an integer
  def uniquePaths(self, m, n):
    table = [[0]*n for i in xrange(m)]

    # table[i][j]: How many possible unique paths when we reach (i, j)
    table[0][0] = 1
    for i in xrange(1, m):
      table[i][0] = table[i-1][0]
    for j in xrange(1, n):
      table[0][j] = table[0][j-1]

    for i in xrange(1, m):
      for j in xrange(1,n):
        table[i][j] = table[i-1][j] + table[i][j-1]

    return table[m-1][n-1]

s = Solution()

print s.uniquePaths(3, 7)
