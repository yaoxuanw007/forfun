# https://oj.leetcode.com/problems/longest-valid-parentheses/

class Solution:
  # @param s, a string
  # @return an integer
  def longestValidParentheses(self, s):
    result, prev, stack = 0, 0, []
    # use index to get length information
    for i in xrange(0, len(s)):
      if s[i] == '(':
        stack.append(i)
      else:
        if len(stack) > 0 and s[stack[-1]] == '(':
          stack.pop()
          prev = -1 if len(stack) == 0 else stack[-1]
          result = max(result, i - prev)
        else:
          stack.append(i)
    return result

s = Solution()

print s.longestValidParentheses("(()"), 2
print s.longestValidParentheses("(()(((()"), 2
print s.longestValidParentheses(")()())"), 4
print s.longestValidParentheses("()"), 2
print s.longestValidParentheses("()(()"), 2
print s.longestValidParentheses("(()(()))"), 8
print s.longestValidParentheses("("), 0
print s.longestValidParentheses(")"), 0
print s.longestValidParentheses(""), 0
