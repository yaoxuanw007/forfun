# https://oj.leetcode.com/problems/combinations/

class Solution:
  # @return a list of lists of integers
  def combine(self, n, k):
    result = [[]]
    while len(result[0]) < k:
      front = result.pop(0)
      startNum, fLen = 1, len(front)
      if fLen > 0:
        startNum = front[-1] + 1
      for i in xrange(startNum, n+1-(k-fLen)+1):
        result.append(front + [i])
    return result

s = Solution()

print s.combine(4, 2)
