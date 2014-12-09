# https://oj.leetcode.com/problems/first-missing-positive/

class Solution:
  # @param A, a list of integers
  # @return an integer
  def firstMissingPositive(self, A):
    result = 0

    aLen = len(A)
    # zero and negative values are useless, set to 0
    for i in xrange(0, aLen):
      if A[i] <= 0:
        A[i] = 0
    # if A[i] > 0: origial value = A[i]
    # elif A[i] < -1: origial value = -1*(A[i]+1)
    # else: orignal value = 0
    #
    # both 0 and -1 are from zero and negative values.
    # But A[i] == -1 means we found integer i+1
    # A[i] == 0 means we don't find integer i+1
    for i in xrange(0, aLen):
      if A[i] > 0 and A[i] <= aLen:
        pos = A[i]-1
        if A[pos] >= 0:
          A[pos] = -1*A[pos] - 1
      elif A[i] < -1 and abs(A[i]+1) <= aLen:
        pos = abs(A[i]+1)-1
        if A[pos] >= 0:
          A[pos] = -1*A[pos] - 1
    # get largest index with negative value
    # before meet first non-negative value
    for i in xrange(0, aLen):
      if A[i] >= 0:
        break
      result = i+1

    return result + 1

s = Solution()

print s.firstMissingPositive([1,2,0])
print s.firstMissingPositive([3,4,-1,1])
print s.firstMissingPositive([1])
