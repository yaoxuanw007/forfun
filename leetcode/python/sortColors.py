# https://oj.leetcode.com/problems/sort-colors/

class Solution:
  # @param A a list of integers
  # @return nothing, sort in place
  def sortColors(self, A):
    # k is the first white index
    i, j, k = 0, len(A) - 1, 0
    while i <= j:
      if A[i] == 0:
        A[i], A[k] = A[k], A[i]
        k += 1
        i += 1
      elif A[i] == 2:
        while i < j and A[j] == 2:
          j -= 1
        A[i], A[j] = A[j], A[i]
        j -= 1
      else:
        i += 1

s = Solution()

A = [2,1,0,2,1,0]
s.sortColors(A)
print A

A = [1,0]
s.sortColors(A)
print A
