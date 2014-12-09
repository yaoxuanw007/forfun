# https://oj.leetcode.com/problems/decode-ways/

class Solution:
  # @param s, a string
  # @return an integer
  def numDecodings(self, s):
    sLen = len(s)
    table = [0] * (sLen + 1)
    if len(s) > 0:
      table[0] = 1
      if int(s[0]) > 0:
        table[1] = 1
    for i in xrange(2, sLen + 1):
      num = int(s[i-2:i])
      if num == 10 or num == 20:
        table[i] = table[i-2]
      elif num % 10 == 0:
        table[i] = 0
      elif num < 10 or num > 26:
        table[i] = table[i-1]
      else:
        table[i] = table[i-1] + table[i-2]
    return table[sLen]

s = Solution()

print s.numDecodings("12")
print s.numDecodings("230")
print s.numDecodings("")
print s.numDecodings("0")
print s.numDecodings("10")
