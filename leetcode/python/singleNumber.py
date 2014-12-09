# https://oj.leetcode.com/problems/single-number/

class Solution:
  # @param A, a list of integer
  # @return an integer
  def singleNumber(self, A):
    result = 0
    for e in A:
     result ^= e
    return result

s = Solution()

print s.singleNumber([6,6,2,3,3,-4,-4])
print s.singleNumber([6,2,3,-4,6,2,-4])
