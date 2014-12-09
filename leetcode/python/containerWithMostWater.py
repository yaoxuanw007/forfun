# https://oj.leetcode.com/problems/container-with-most-water/

class Solution:
  # @return an integer
  def maxArea(self, height):
    result, i, j = 0, 0, len(height) - 1
    while i < j:
      area = (j - i) * min(height[i], height[j])
      if area > result:
        result = area
      elif height[i] > height[j]:
        j -= 1
      else:
        i += 1
    return result
