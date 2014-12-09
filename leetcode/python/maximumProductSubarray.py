# Question
#
# Find the contiguous subarray within an array (containing
# at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#
# Link: https://oj.leetcode.com/problems/maximum-product-subarray/

# The contiguous subarray which has the largest product and
# the last element
# [2]               => 2, 2
# [2,3]             => 6, 3
# [2,3,-2]          => -2,-12
# [2,3,-2,4]        => 4,-48
#
# Dynamic Programming

class Solution:
  # @param A, a list of integers
  # @return an integer
  def maxProduct(self, A):
    positive, negative = [A[0]], [A[0]]
    for i in xrange(1, len(A)):
      if A[i] >= 0:
        positive.append(max(positive[i-1]*A[i], A[i]))
        negative.append(min(negative[i-1]*A[i], A[i]))
      else:
        negative.append(min(positive[i-1]*A[i], A[i]));
        positive.append(max(negative[i-1]*A[i], A[i]));
    return reduce(lambda x, y: x if x >= y else y,
        iter(positive[1:]), positive[0])

s = Solution()

nums = [
    [2,3,-2,4],
    [2,3,0,4],
    [2,3,-2,4,6],
    [2,3,-2,4,6,-1],
    ]

for num in nums:
  print s.maxProduct(num)
