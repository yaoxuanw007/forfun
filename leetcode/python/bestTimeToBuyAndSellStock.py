# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):
    total = 0
    if len(prices) > 0:
      min = prices[0]
      for i in xrange(1, len(prices)):
        if min > prices[i]:
          min = prices[i]
        elif prices[i] - min > total:
          total = prices[i] - min
    return total

s = Solution()

print s.maxProfit([2,1,4,1,5])
