# https://oj.leetcode.com/problems/triangle/

class Solution:
  # @param triangle, a list of lists of integers
  # @return an integer
  # If not modify triangle, then use array to keep the information of last row
  def minimumTotal(self, triangle):
    result, tLen = 0, len(triangle)
    if tLen > 0:
      for i in xrange(1, tLen):
        for j in xrange(0, i+1):
          if j == 0:
            triangle[i][j] += triangle[i-1][j]
          elif j == i:
            triangle[i][j] += triangle[i-1][-1]
          else:
            triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
      result = min(triangle[-1])
    return result

s = Solution()

print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

