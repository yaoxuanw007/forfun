# https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
  # @param tokens, a list of string
  # @return an integer
  def evalRPN(self, tokens):
    stack, operators = [], set(['+', '-', '*', '/'])
    for token in tokens:
      if token in operators:
        n2, n1 = stack.pop(), stack.pop()
        stack.append(self.calculate(n1, n2, token))
      else:
        stack.append(int(token))
    return stack[0] if len(stack) > 0 else 0

  def calculate(self, n1, n2, operator):
    if operator == '+':
      return n1 + n2
    elif operator == '-':
      return n1 - n2
    elif operator == '*':
      return n1 * n2
    else: # /
      sign = 1
      if n1 < 0 and n2 > 0:
        n1 = -1 * n1
        sign = -1
      elif n1 > 0 and n2 < 0:
        n2 = -1 * n2
        sign = -1
      return sign * (n1 / n2)

s = Solution()

print s.evalRPN(["2", "1", "+", "3", "*"]), 9
print s.evalRPN(["4", "13", "5", "/", "+"]), 6
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22
