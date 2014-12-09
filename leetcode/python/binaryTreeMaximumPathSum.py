# https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return an integer
  def maxPathSum(self, root):
    # return max(self.findMaxRecur(root))
    self.maxVal = None
    self.findMax(root)
    return 0 if self.maxVal == None else self.maxVal

  def findMax(self, root):
    if root == None:
      return 0
    else:
      left = self.findMax(root.left)
      right = self.findMax(root.right)
      valRoot = max(root.val, root.val + left, root.val + right)
      val = max(valRoot, root.val + left + right)
      if self.maxVal == None or self.maxVal < val:
        self.maxVal = val
    return valRoot

s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print s.maxPathSum(root)

root = TreeNode(-3)
print s.maxPathSum(root)

root = None
print s.maxPathSum(root)

root = TreeNode(2)
root.right = TreeNode(-1)
print s.maxPathSum(root)

root = TreeNode(-1)
root.right = TreeNode(2)
print s.maxPathSum(root)
