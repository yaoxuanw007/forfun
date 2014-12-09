# https://oj.leetcode.com/problems/reverse-integer/

class Solution:
  # @return an integer
  def reverse(self, x):
    result, sign, maxInt = 0, 1, int(bin(2**31), 2)

    if x < 0:
      sign = -1
      x *= -1

    while x > 0:
      result = result * 10 + x % 10
      x /= 10
      if result > maxInt:
        return 0

    return sign * result

s = Solution()

print s.reverse(123), 321
print s.reverse(-123), -321
print s.reverse(100), 1
print s.reverse(2147483647), 0
print s.reverse(1563847412), 0
