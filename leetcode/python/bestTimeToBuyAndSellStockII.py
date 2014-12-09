# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):
    total = 0
    for i in xrange(1, len(prices)):
      if prices[i] > prices[i-1]:
        total += prices[i] - prices[i-1]
    return total

s = Solution()

print s.maxProfit([2,1,3])
