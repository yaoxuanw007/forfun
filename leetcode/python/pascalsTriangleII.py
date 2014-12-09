# https://oj.leetcode.com/problems/pascals-triangle-ii/

class Solution:
  # @return a list of integers
  def getRow(self, rowIndex):
    prev, curr = [], []
    for i in xrange(0, rowIndex+1):
      curr = []
      for j in xrange(0, i+1):
        if j == 0 or j == i:
          curr.append(1)
        else:
          curr.append(prev[j-1] + prev[j])
      prev = curr
    return curr

s = Solution()

print s.getRow(0)
print s.getRow(1)
print s.getRow(3)
