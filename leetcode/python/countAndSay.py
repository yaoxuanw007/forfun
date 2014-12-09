# https://oj.leetcode.com/problems/count-and-say/

# 10:56 - 11:11

class Solution:
  # @return a string
  def countAndSay(self, n):
    result = "1"
    # n == 1, result == '1', not when n == 0
    for i in xrange(1, n):
      last, count, nextResult = result[0], 1, ""
      for j in xrange(1, len(result)):
        curr = result[j]
        if last != curr:
          nextResult += str(count) + str(last)
          count = 0
        count += 1
        last = curr
      nextResult += str(count) + str(last)
      result = nextResult
    return result

s = Solution()

print s.countAndSay(1), '1'
print s.countAndSay(2), '11'
print s.countAndSay(3), '21'
print s.countAndSay(4), '1211'
print s.countAndSay(5), '111221'
