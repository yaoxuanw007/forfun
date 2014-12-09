# https://oj.leetcode.com/problems/merge-sorted-array/

# 11:13 - 11:45

# Assume that both A and B is ascending
class Solution:
  # @param A  a list of integers
  # @param m  an integer, length of A
  # @param B  a list of integers
  # @param n  an integer, length of B
  # @return nothing
  def merge(self, A, m, B, n):

    # copy from the end of array
    # leave first n element empty
    for i in xrange(m-1, -1, -1):
      A[i+n] = A[i]

    i, j, k = 0, 0, 0
    while i < m or j < n:
      if i < m and j < n:
        if A[n+i] < B[j]:
          A[k] = A[n+i]
          i += 1
        else:
          A[k] = B[j]
          j += 1
      elif i < m:
        A[k] = A[n+i]
        i += 1
      elif j < n:
        A[k] = B[j]
        j += 1
      k += 1

s = Solution()

A = [1,4,5,0,0,0]
aLen = 3
B = [2,8]
bLen = 2
s.merge(A, aLen, B, bLen)
print A

A = [1]
aLen = 1
B = []
bLen = 0
s.merge(A, aLen, B, bLen)
print A

A = [4, 0, 0, 0, 0, 0]
aLen = 1
B = [1,2,3,5,6]
bLen = 5
s.merge(A, aLen, B, bLen)
print A

A = [1,2,4,5,6,0]
aLen = 5
B = [3]
bLen =  1
s.merge(A, aLen, B, bLen)
print A
