# https://oj.leetcode.com/problems/jump-game/

class Solution:
  # @param A, a list of integers
  # @return a boolean
  def canJump(self, A):
    if len(A) == 0:
      return False

    table = [False] * len(A)
    # stand on the first piece
    table[0] = True
    for i in xrange(0, len(A)-1):
      if not table[i]:
        continue
      for j in xrange(A[i], 0, -1):
        next = i + j
        if next >= len(A) - 1:
          return True
        # If table[next] == True,
        # table[i] ... table[next] should be true and skip it
        if table[next]:
          break
        table[next] = True
    return table[-1]

s =  Solution()

print s.canJump([2,3,1,1,4]), True
print s.canJump([3,2,1,0,4]), False
