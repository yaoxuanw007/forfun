# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

# 12:24 - 12:36

class Solution:
  # @param a list of integers
  # @return an integer
  def removeDuplicates(self, A):
    # next means the next index which can be used to add element
    # next = length
    aLen, next = len(A), 0
    if aLen > 0:
      last, next = 0, 1
      for i in xrange(1, aLen):
        if A[last] == A[i]:
          continue
        else:
          A[next] = A[i]
          next += 1
          last = i
    return next

s = Solution()

print s.removeDuplicates([1,1,2])
print s.removeDuplicates([1,1])
print s.removeDuplicates([1])
print s.removeDuplicates([])
