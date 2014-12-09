# https://oj.leetcode.com/problems/permutations-ii/

class Solution:
  # @param num, a list of integer
  # @return a list of lists of integers
  def permuteUnique(self, num):
    if len(num) == 0:
      return []
    num = sorted(num)
    result = [num[:]]
    while True:
      nextNum, isEnd = self.nextPermutation(num)
      if isEnd:
        break
      result.append(nextNum[:])
    return result

  def nextPermutation(self, num):
    i = len(num) - 2
    while i >= 0 and num[i] >= num[i+1]:
      i -= 1
    if i >= 0:
      j = len(num) - 1
      while j >= 0 and num[i] >= num[j]:
        j -= 1
      num[i], num[j] = num[j], num[i]
    self.reversed(num, i+1)
    return (num, True if i < 0 else False)

  def reversed(self, num, start):
    i, j = start, len(num) - 1
    while i < j:
      num[i], num[j] = num[j], num[i]
      i += 1
      j -= 1

s = Solution()

print s.permuteUnique([1,1,2])
