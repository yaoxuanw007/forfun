# https://oj.leetcode.com/problems/generate-parentheses/

class Solution:
  # @param an integer
  # @return a list of string
  def generateParenthesis(self, n):
    self.result = []
    self.parentheses(n, n, "")
    return self.result

  def parentheses(self, left, right, comb):
    if left < 0 or left > right:
      return
    if left == 0 and right == 0:
      self.result.append(comb)
    else:
      self.parentheses(left - 1, right, comb + "(")
      self.parentheses(left, right - 1, comb + ")")

s = Solution()

print s.generateParenthesis(3)
