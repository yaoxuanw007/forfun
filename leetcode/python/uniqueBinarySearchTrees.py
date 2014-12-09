# https://oj.leetcode.com/problems/unique-binary-search-trees/

class Solution:
  # @return an integer
  def numTrees(self, n):
    if n <= 1:
      return 1
    total = 0
    for i in xrange(n):
      total += self.numTrees(i) * self.numTrees(n-i-1)
    return total

s = Solution()

print s.numTrees(3)
