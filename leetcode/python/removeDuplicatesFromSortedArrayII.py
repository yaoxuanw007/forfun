# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
  # @param A a list of integers
  # @return an integer
  def removeDuplicates(self, A):
    k, count = 0, 0
    for i in xrange(len(A)):
      if i > 0 and A[i] == A[i-1]:
        count += 1
        if count >= 2:
          continue
      else:
        count = 0
      if k != i:
        A[k] = A[i]
      k += 1
    return k

s = Solution()

print s.removeDuplicates([1,1,1,2,2,3])
print s.removeDuplicates([1,1,1,2])
print s.removeDuplicates([1])
print s.removeDuplicates([])
