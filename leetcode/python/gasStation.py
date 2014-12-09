# https://oj.leetcode.com/problems/gas-station/

class Solution:
  # @param gas, a list of integers
  # @param cost, a list of integers
  # @return an integer
  def canCompleteCircuit(self, gas, cost):
    n = len(gas)
    if n == 0:
      return -1
    startIndex, total = 0, 0
    for i in xrange(2*n):
      j = i % n
      if startIndex != i and startIndex == j:
        break
      total += gas[j] - cost[j]
      if total < 0:
        if i < n - 1:
          startIndex = i + 1
          total = 0
        else:
          startIndex = -1
          break
    return startIndex

s = Solution()

print s.canCompleteCircuit([1,2], [2,1])
print s.canCompleteCircuit([4], [5])
print s.canCompleteCircuit([5], [4])
