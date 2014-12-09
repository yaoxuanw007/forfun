# https://oj.leetcode.com/problems/add-binary/

# 13:14 - 13:27

class Solution:
  # @param a, a string
  # @param b, a string
  # @return a string
  def addBinary(self, a, b):
    result, aLen, bLen = "", len(a), len(b)
    accum = 0
    for i in xrange(0, max(aLen, bLen)):
      aElem, bElem = 0, 0
      if i < aLen:
        aElem = int(a[-1 - i])
      if i < bLen:
        bElem = int(b[-1 - i])
      sum = aElem + bElem + accum
      accum = sum / 2
      result = str(sum % 2) + result
    if accum == 1:
      result = '1' + result
    return result

s = Solution()

print s.addBinary('11', '111')
print s.addBinary('1', '111')
