# https://oj.leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
  # @param height, a list of integer
  # @return an integer
  def largestRectangleArea(self, height):
    result, hStack, cStack = 0, [], []
    # add 0 as last height to pop out all heights
    for h in height + [0]:
      count = 0
      while len(hStack) > 0 and hStack[-1] > h:
        count += cStack[-1]
        result = max(result, hStack[-1] * count)
        hStack.pop()
        cStack.pop()
      hStack.append(h)
      # push the total count of popped bar heights and itself
      cStack.append(count + 1)
    return result

s = Solution()

print s.largestRectangleArea([2,1,5,6,2,3])



