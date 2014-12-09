# https://oj.leetcode.com/problems/search-insert-position/

class Solution:
  # @param A, a list of integers
  # @param target, an integer to be inserted
  # @return integer
  def searchInsert(self, A, target):
    for i in xrange(len(A)):
      if A[i] >= target:
        return i
    return len(A)

s = Solution()

print s.searchInsert([1,3,5,6], 5), 2
print s.searchInsert([1,3,5,6], 2), 1
print s.searchInsert([1,3,5,6], 7), 4
print s.searchInsert([1,3,5,6], 0), 0
