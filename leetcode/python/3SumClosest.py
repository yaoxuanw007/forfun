# https://oj.leetcode.com/problems/3sum-closest/

class Solution:
  # @return an integer
  def threeSumClosest(self, num, target):
    num = sorted(num)
    result, minDiff = -1, -1
    for i in xrange(len(num)-2):
      j, k = i+1, len(num)-1
      while j < k:
        val = num[i] + num[j] + num[k]
        diff = val - target
        if minDiff < 0 or minDiff > 0 and abs(diff) < minDiff:
          minDiff = abs(diff)
          result = val
        if diff == 0:
          break
        elif diff > 0:
          k -= 1
        else:
          j += 1
    return result

s = Solution()

print s.threeSumClosest([-1,2,1,-4], 1), 2
print s.threeSumClosest([0,1,2], 3), 3
