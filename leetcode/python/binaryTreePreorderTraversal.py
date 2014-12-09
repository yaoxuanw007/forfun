# https://oj.leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return a list of integers
  def preorderTraversal(self, root):
    # return self.preorderR(root)
    return self.preorderI(root)

  def preorderR(self, root):
    if root == None:
      return []
    left = self.preorderR(root.left)
    right = self.preorderR(root.right)
    return [root.val] + left + right

  def preorderI(self, root):
    if root == None:
      return []
    result, stack = [], [root]
    while len(stack) > 0:
      top = stack.pop(-1)
      if top.right != None:
        stack.append(top.right)
      if top.left != None:
        stack.append(top.left)
      result.append(top.val)
    return result

s = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print s.preorderTraversal(root)
