# https://oj.leetcode.com/problems/implement-strstr/

# 12:55 - 13:03

class Solution:
  # @param haystack, a string
  # @param needle, a string
  # @return an integer
  def strStr(self, haystack, needle):
    hLen, nLen = len(haystack), len(needle)
    for i in xrange(0, hLen - nLen + 1):
      if haystack[i:i+nLen] == needle:
        return i
    return -1

# More: Rabin-Karp algorithm, KMP algorithm, and the Boyer- Moore algorithm

s = Solution()
print s.strStr('123', '23')
print s.strStr('12323', '23')
print s.strStr('1', '23')
print s.strStr('123', '')
print s.strStr('123', '4')
print s.strStr('', '')
