# https://oj.leetcode.com/problems/gray-code/

class Solution:
  # @return a list of integers
  def grayCode(self, n):
    result, prefix = [0], 1
    for i in xrange(0, n):
      rLen = len(result)
      for j in xrange(rLen):
        result.append(prefix + result[rLen-1-j])
      prefix <<= 1
    return result

s = Solution()

print s.grayCode(2)
print s.grayCode(1)
print s.grayCode(0)
