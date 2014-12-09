# https://oj.leetcode.com/problems/min-stack/

# 17:32 - 18;30

class MinStack:

  def __init__(self):
    # minStk is for index of min value
    self.minStk = []
    self.valStk = []

  # @param x, an integer
  # @return an integer
  def push(self, x):
    if len(self.valStk) == 0 or x < self.valStk[self.minStk[-1][0]]:
      # use index to avoid out of memory
      self.minStk.append([len(self.valStk), 1])
    elif len(self.valStk) > 0:
      self.minStk[-1][1] += 1
    self.valStk.append(x)

  # @return nothing
  def pop(self):
    if len(self.valStk) > 0:
      if self.minStk[-1][1] == 1:
        self.minStk.pop()
      else:
        self.minStk[-1][1] -= 1
      self.valStk.pop()

  # @return an integer
  def top(self):
    if len(self.valStk) > 0:
      return self.valStk[-1]
    return None

  # @return an integer
  def getMin(self):
    if len(self.valStk) > 0:
      return self.valStk[self.minStk[-1][0]]
    return None

s = MinStack()

s.push(8)
s.push(1)
s.push(2)
print s.getMin(), 1
print s.pop()
print s.top(), 1
print s.pop()
print s.getMin(), 8
print s.push(5)
print s.top(), 5
print s.getMin(), 5

s = MinStack()

s.push(0)
s.push(1)
s.push(0)
print s.getMin()
s.pop()
print s.getMin()
s.pop()
print s.getMin()
s.pop()
