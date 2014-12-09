# https://oj.leetcode.com/problems/minimum-path-sum/

class Solution:
  # @param grid, a list of lists of integers
  # @return an integer
  def minPathSum(self, grid):
    if len(grid) == 0 or len(grid[0]) == 0:
      return 0

    m, n = len(grid), len(grid[0])
    table = [[0]*n for i in xrange(m)]

    table[0][0] = grid[0][0]
    for i in xrange(1, m):
      table[i][0] = table[i-1][0] + grid[i][0]
    for j in xrange(1, n):
      table[0][j] = table[0][j-1] + grid[0][j]

    for i in xrange(1, m):
      for j in xrange(1, n):
        table[i][j] = min(table[i-1][j], table[i][j-1]) + grid[i][j]

    return table[m-1][n-1]

s = Solution()

print s.minPathSum([[1,1,3], [2,1,3], [3,1,1]])
