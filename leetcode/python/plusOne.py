# https://oj.leetcode.com/problems/plus-one/

# 13:04 - 13:11

class Solution:
  # @param digits, a list of integer digits
  # @return a list of integer digits
  def plusOne(self, digits):
    dLen, accum = len(digits), 0
    for i in xrange(dLen - 1, -1, -1):
      sum = digits[i] + 1
      digits[i] = sum % 10
      accum = sum / 10
      if accum == 0:
        break
    if accum == 1:
      digits.insert(0, accum)
    return digits

s = Solution()

print str(s.plusOne([0]))
print str(s.plusOne([1,9,9]))
print str(s.plusOne([1,2,8]))
print str(s.plusOne([9,9,9]))
