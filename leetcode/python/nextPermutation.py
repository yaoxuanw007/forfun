# https://oj.leetcode.com/problems/next-permutation/

class Solution:
  # @param num, a list of integer
  # @return a list of integer
  def nextPermutation(self, num):
    i = len(num)-2
    while i >= 0 and num[i] >= num[i+1]:
      i -= 1
    if i >= 0:
      j = len(num) - 1
      # If we use same value, it would be same
      while j >= 0 and num[i] >= num[j]:
        j -= 1
      num[i], num[j] = num[j], num[i]
    self.reversed(num, i+1)
    return num

  def reversed(self, num, start):
    i, j = start, len(num)-1
    while i < j:
      num[i], num[j] = num[j], num[i]
      i += 1
      j -= 1

s = Solution()

print s.nextPermutation([1,2,3]), [1,3,2]
print s.nextPermutation([3,2,1]), [1,2,3]
print s.nextPermutation([1,1,5]), [1,5,1]
