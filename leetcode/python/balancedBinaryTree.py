# https://oj.leetcode.com/problems/balanced-binary-tree/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# 10:30 - 10:42

class Solution:
  # @param root, a tree node
  # @return a boolean
  def isBalanced(self, root):
    # Empty tree is balanced
    if root == None:
      return True
    b, h = self.balanced(root)
    return b

  def balanced(self, root):
    bLeft, hLeft = True, 0
    if root.left != None:
      bLeft, hLeft = self.balanced(root.left)

    # skip the rest if tree is not balanced until now
    b = bLeft

    bRight, hRight = True, 0
    if b and root.right != None:
      bRight, hRight = self.balanced(root.right)

    b = b and bRight and abs(hLeft - hRight) <= 1
    h = max(hLeft, hRight) + 1

    return [b, h]

s = Solution()

root = None
print s.isBalanced(root)

root = TreeNode(1)
print s.isBalanced(root)

root = TreeNode(1)
root.left = TreeNode(1)
print s.isBalanced(root)

root = TreeNode(1)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
print s.isBalanced(root)
