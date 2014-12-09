# https://oj.leetcode.com/problems/divide-two-integers/
# credit: https://oj.leetcode.com/discuss/16208/my-fast-solution-using-bit-operation

# devidend = sign * (e[x] * 2^x + e[x-1] * 2^(x-1) + ... + e[0] * 2^0) * divisor
# e[i] = 0 or 1
# result = sign * (e[x] * 2^x + e[x-1] * 2^(x-1) + ... + e[0] * 2^0)
class Solution:
  # @return an integer
  def divide(self, dividend, divisor):
    result = 0
    sign = 1
    if dividend < 0:
      dividend = -dividend
      sign = -sign
    if divisor < 0:
      divisor = -divisor
      sign = -sign

    while dividend >= divisor:
      # d = divisor << x, i = 1 << x
      d, i = divisor, 1
      while d < dividend:
        d <<= 1
        i <<= 1
      if d > dividend:
        d >>= 1
        i >>= 1
      dividend -= d
      result += i

    if result > 0 and sign < 0:
      result = -result
    return result

s = Solution()

print s.divide(123, 5), 24
print s.divide(125, 5), 25

