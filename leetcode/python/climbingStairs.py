# https://oj.leetcode.com/problems/climbing-stairs/

# 12:45 - 12:54

class Solution:
  # @param n, an integer
  # @return an integer
  def climbStairs(self, n):
    table = [0] * (n+1)
    table[0] = 0
    if n >= 1:
      table[1] = 1
    if n >= 2:
      table[2] = 2
    for i in xrange(3, n+1):
      table[i] = table[i-1] + table[i-2]
    return table[n]

s = Solution()
print s.climbStairs(0)
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(3)
