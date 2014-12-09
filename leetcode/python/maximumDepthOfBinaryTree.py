# https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# 11:02 - 11:08

class Solution:
  # @param root, a tree node
  # @return an integer
  def maxDepth(self, root):
    if root == None:
      return 0
    self.result = -1
    self.getMaxDepth(root, 0)
    return self.result

  def getMaxDepth(self, root, depth):
    if root == None:
      return
    depth += 1
    if root.left == None and root.right == None:
      if self.result < 0 or self.result < depth:
        self.result = depth
      return
    self.getMaxDepth(root.left, depth)
    self.getMaxDepth(root.right, depth)

s = Solution()

root = None
print s.maxDepth(root)

root = TreeNode(1)
root.left = TreeNode(1)
print s.maxDepth(root)
