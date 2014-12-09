# https://oj.leetcode.com/problems/unique-paths-ii/

class Solution:
  # @param obstacleGrid, a list of lists of integers
  # @return an integer
  def uniquePathsWithObstacles(self, obstacleGrid):
    if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
      return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    table = [[0]*n for i in xrange(m)]
    table[0][0] = 1
    for i in xrange(1, m):
      if obstacleGrid[i][0] == 1:
        table[i][0] = 0
      else:
        table[i][0] = table[i-1][0]
    for j in xrange(1, n):
      if obstacleGrid[0][j] == 1:
        table[0][j] = 0
      else:
        table[0][j] = table[0][j-1]

    for i in xrange(1, m):
      for j in xrange(1, n):
        if obstacleGrid[i][j] == 1:
          table[i][j] = 0
        else:
          table[i][j] = table[i-1][j] + table[i][j-1]

    return table[m-1][n-1]

s = Solution()

print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2
