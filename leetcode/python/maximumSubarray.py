# https://oj.leetcode.com/problems/maximum-subarray/

class Solution:
  # @param A, a list of integers
  # @return an integer
  def maxSubArray(self, A):
    # maxSums[i] = the max sum of contiguous subarray with A[i]
    maxSums = [0] * len(A)
    if len(maxSums) > 0:
      maxSums[0] = A[0]
      for i in xrange(1, len(maxSums)):
        if maxSums[i-1] < 0:
          maxSums[i] = A[i]
        else:
          maxSums[i] = maxSums[i-1] + A[i]
    return max(maxSums)

s = Solution()

print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6
