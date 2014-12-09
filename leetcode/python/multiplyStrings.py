# https://oj.leetcode.com/problems/multiply-strings/

class Solution:
  # @param num1, a string
  # @param num2, a string
  # @return a string
  def multiply(self, num1, num2):
    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)
    for i in xrange(0, len1):
      carry = 0
      for j in xrange(0, len2):
        carry = int(num1[len1-1-i]) * int(num2[len2-1-j]) + result[i+j] + carry
        result[i+j] = carry % 10
        carry /= 10
      # put carry in result, reset carry
      # high to low in result is from end to front
      result[i+len2] = carry

    k = len1 + len2 - 1
    # clear all zero in the high digit, except the last digit
    while k > 0 and result[k] == 0:
      k -= 1

    return reduce(lambda x,y: x+y, [str(result[k-i]) for i in xrange(0,k+1)])

s = Solution()

print s.multiply("12", "12")
