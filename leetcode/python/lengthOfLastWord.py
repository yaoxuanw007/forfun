# https://oj.leetcode.com/problems/length-of-last-word/

# 17:03 - 17:09

class Solution:
  # @param s, a string
  # @return an integer
  def lengthOfLastWord(self, s):
    result, foundEmpty = 0, False
    for c in s:
      if not c.isalpha():
        foundEmpty = True
        continue
      if foundEmpty:
        result = 0
        foundEmpty = False
      result += 1
    return result

s = Solution()
print s.lengthOfLastWord("hello world")

