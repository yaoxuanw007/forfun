# https://oj.leetcode.com/problems/valid-palindrome/

class Solution:
  # @param s, a string
  # @return a boolean

  # create a new string
  def isPalindrome1(self, s):
    str = [c.lower() for c in s if c.isalnum()]
    n = len(str)
    for i in xrange(0, n/2):
      if str[i] != str[n-1-i]:
        return False
    return True

  # constant space
  def isPalindrome(self, s):
    i, j = 0, len(s)-1
    while i < j:
      while i < j and not s[i].isalnum():
        i += 1
      while i < j and not s[j].isalnum():
        j -= 1
      if s[i].lower() != s[j].lower():
        return False
      i += 1
      j -= 1
    return True

s = Solution()

print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("race a car")

