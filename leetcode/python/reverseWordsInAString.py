# https://oj.leetcode.com/problems/reverse-words-in-a-string/

class Solution:
  # @param s, a string
  # @return a string
  def reverseWords(self, s):
    result, word, s = [], "", s[::-1]
    for i in xrange(len(s)):
      if s[i] != " ":
        word += s[i]
      elif word != "":
        result.append(word[::-1])
        word = ""
    if word != "":
      result.append(word[::-1])
    return " ".join(result)

  # TODO: try one-pass

s = Solution()

print s.reverseWords(" the sky is blue ")
