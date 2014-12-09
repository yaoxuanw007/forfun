# https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# NOTE: a height balanced BST

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param num, a list of integers
  # @return a tree node
  def sortedArrayToBST(self, num):
    return self.arrayToBST(num, 0, len(num) - 1)

  def arrayToBST(self, num, start, end):
    root = None
    if start <= end:
      mid = (start + end) / 2
      root = TreeNode(num[mid])
      root.left = self.arrayToBST(num, start, mid - 1)
      root.right = self.arrayToBST(num, mid + 1, end)
    return root
