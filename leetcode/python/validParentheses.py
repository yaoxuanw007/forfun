# https://oj.leetcode.com/problems/valid-parentheses/

# 12:07 - 12:13

class Solution:
  # @return a boolean
  def isValid(self, s):
    stack, map = [], {'(':')', '[':']', '{': '}'}
    for c in s:
      if c == '(' or c == '[' or c == '{':
        stack.append(c)
      elif len(stack) > 0 and map[stack[-1]] == c:
        stack.pop()
      else:
        return False
    return len(stack) == 0

s = Solution()

print s.isValid("()[]{}")
print s.isValid("()")
print s.isValid("(]")
print s.isValid("([)]")
print s.isValid("]")
