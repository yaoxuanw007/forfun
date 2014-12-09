# https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# 10:09 - 10:25

class Solution:
  # @param root, a tree node
  # @return an integer
  def minDepth(self, root):
    if root == None:
      return 0
    self.result = -1
    self.findMinDepth(root, 0)
    return self.result

  def findMinDepth(self, root, depth):
    if root == None:
      return

    if self.result >= 0 and depth >= self.result:
      return

    depth += 1
    if root.left == None and root.right == None:
      if self.result < 0 or self.result > depth:
        self.result = depth
        return
    self.findMinDepth(root.left, depth)
    self.findMinDepth(root.right, depth)

s = Solution()

root = None
print s.minDepth(root)

root = TreeNode(1)
print s.minDepth(root)

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
print s.minDepth(root)
