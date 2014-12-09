# https://oj.leetcode.com/problems/remove-element/

# 12:38 - 12:44

class Solution:
  # @param    A       a list of integers
  # @param    elem    an integer, value need to be removed
  # @return an integer
  def removeElement(self, A, elem):
    aLen = len(A)
    if aLen > 0:
      i = 0
      while i < aLen:
        if A[i] == elem:
          A[i] = A[aLen-1]
          aLen -= 1
          continue
        i += 1
    return aLen

s = Solution()

print s.removeElement([], 2)
print s.removeElement([2,2,2], 2)
print s.removeElement([1,2,3,2,4,2], 2)
