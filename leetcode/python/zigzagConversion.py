# https://oj.leetcode.com/problems/zigzag-conversion/

# 10:25 - 10:56

class Solution:
  # @return a string
  def convert(self, s, nRows):
    result, sLen = "", len(s)
    for i in xrange(0, nRows):
      # if nRows == 1, countPerGroup = 0 and we set it to 1
      countPerGroup = nRows * 2 -2 or 1
      countGroup = sLen / countPerGroup
      if sLen % countPerGroup > 0:
        countGroup += 1
      for j in xrange(0, countGroup):
        firstIndex = countPerGroup * j + i
        # check out of range issue
        if firstIndex < sLen:
          result += s[firstIndex]
        if i > 0 and i < nRows - 1:
          secondIndex = countPerGroup * j + countPerGroup - i
          if secondIndex < sLen:
            result += s[secondIndex]
    return result

s = Solution()

print s.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"
print s.convert("PAYPALISHIRING", 0), ""
print s.convert("PAYPALISHIRING", 1), "PAHNAPLSIIGYIR"
print s.convert("PA", 3), "PA"
print s.convert("PA", 1), "pA"
print s.convert("", 3), ""
