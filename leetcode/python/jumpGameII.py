# https://oj.leetcode.com/problems/jump-game-ii/

class Solution:
  # @param A, a list of integers
  # @return an integer

  # greedy
  def jump(self, A):
    result, curr, dest = 0, 0, len(A)-1
    while curr < dest:
      maxJump, next = curr, curr
      for i in xrange(1, A[curr]+1):
        if curr + i >= dest:
          next = curr + i
          break
        currJump = curr + i + A[curr + i]
        if maxJump < currJump:
          maxJump = currJump
          next = curr + i
      result += 1
      curr = next
    return result

  # DP
  def jump1(self, A):
    track, n = [0], len(A)
    for i in xrange(1, n):
      for j in xrange(0, i):
        prev = n
        if j+A[j] >= i and prev > track[j]:
          prev = track[j]
          # track is ascending, so break
          break
      track.append(prev + 1)
    return track[-1]

s = Solution()

print s.jump([2,3,1,1,4])
print s.jump([3,2,1])
print s.jump1([2,1,2,1,4])

print s.jump1([2,3,1,1,4])
print s.jump1([3,2,1])
print s.jump1([2,1,2,1,4])
