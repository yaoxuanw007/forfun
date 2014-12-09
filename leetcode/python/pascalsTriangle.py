# https://oj.leetcode.com/problems/pascals-triangle/

class Solution:
  # @return a list of lists of integers
  def generate(self, numRows):
    result = []
    for i in xrange(0, numRows):
      row = []
      for j in xrange(0, i+1):
        if j == 0 or j == i:
          row.append(1)
        else:
          row.append(result[i-1][j-1] + result[i-1][j])
      result.append(row)
    return result

s = Solution()

print s.generate(0)
print s.generate(1)
print s.generate(2)
print s.generate(5)
