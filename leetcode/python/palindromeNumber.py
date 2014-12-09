# https://oj.leetcode.com/problems/palindrome-number/

class Solution:
  # @return a boolean
  def isPalindrome(self, x):
    if x < 0:
      return False
    small, big = 1, 10
    while big <= x:
      big *= 10
    big /= 10
    while small <= big:
      if x/small%10 != x/big%10:
        return False
      small *= 10
      big /= 10
    return True

s = Solution()

print s.isPalindrome(-1), False
print s.isPalindrome(10), False
print s.isPalindrome(11), True
print s.isPalindrome(121), True
