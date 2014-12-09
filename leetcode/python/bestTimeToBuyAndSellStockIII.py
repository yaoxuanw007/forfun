# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# DP
class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):

    if len(prices) == 0:
      return 0

    size = len(prices)
    totals = [0] * size

    curr, diff = prices[0], 0
    # the max profit in xrange(0,i)
    # curr = min value until day i
    # diff = the max profit until day i
    for i in xrange(0, size):
      if prices[i] > curr:
        diff = max(diff, prices[i] - curr)
      else:
        curr = prices[i]
      totals[i] += diff

    # the max profit in xrange(j,len(prices))
    # curr = max value from day j
    # diff = the max profit from day j
    curr, diff = prices[size-1], 0
    for j in xrange(size-1, -1, -1):
      if prices[j] < curr:
        diff = max(diff, curr - prices[j])
      else:
        curr = prices[j]
      totals[j] += diff

    return max(totals)

s = Solution()

print s.maxProfit([1, 2, 3])
print s.maxProfit([2,1,2,0,1])
