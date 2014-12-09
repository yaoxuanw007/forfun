# https://oj.leetcode.com/problems/permutation-sequence/

import math

class Solution:
  # @return a string
  def getPermutation(self, n, k):
    # Given (n, k) == (4,21), four groups: 1***, 2***, 3***, 4***,
    # k = k - 1 to make sure id is index of groups
    # group index that permutation belongs to = k / (3)!
    # next k = k % (3)!
    result, k = [], k - 1
    digits, factorial = range(1, n+1), math.factorial(n)
    for i in xrange(n, 0, -1):
      id, k = divmod(k, factorial / i)
      result.append(digits.pop(id))
      factorial /= i
    return ''.join([str(x) for x in result])

  # Time: O(n*k); Space: O(n)
  # TLE
  # def getPermutation(self, n, k):
  #   # find the start point
  #   factor, d = 1, 0
  #   for i in xrange(1, n+1):
  #     factor *= i
  #     if factor >= k:
  #       if factor == k:
  #         d = i
  #       else:
  #         factor /= i
  #         d = i - 1
  #       k -= factor
  #       break

  #   result = range(1, n+1)
  #   self.reversed(result, n - d)

  #   for i in xrange(k):
  #     self.nextPermutation(result)
  #   return reduce(lambda x,y: x + str(y), result, "")

  # def nextPermutation(self, num):
  #   i = len(num) - 2
  #   while i >= 0 and num[i] >= num[i+1]:
  #     i -= 1
  #   if i >= 0:
  #     j = len(num) - 1
  #     while j >= 0 and num[i] >= num[j]:
  #       j -= 1
  #     num[i], num[j] = num[j], num[i]
  #   self.reversed(num, i+1)

  # def reversed(self, num, start):
  #   i, j = start, len(num) - 1
  #   while i < j:
  #     num[i], num[j] = num[j], num[i]
  #     i += 1
  #     j -= 1

s = Solution()

print s.getPermutation(3, 1), "123"
print s.getPermutation(3, 2), "132"
print s.getPermutation(3, 3), "213"
print s.getPermutation(3, 4), "231"
print s.getPermutation(3, 5), "312"
print s.getPermutation(3, 6), "321"
