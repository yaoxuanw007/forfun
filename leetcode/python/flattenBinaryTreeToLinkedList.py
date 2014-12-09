# https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return nothing, do it in place
  def flatten(self, root):
    # self.preorderR(root)
    self.preorderI(root)
    return root

  # @return last node in preorder
  def preorderR(self, root):
    if root == None:
      return None
    result, right = root, root.right
    last = self.preorderR(root.left)
    if last != None:
      last.right = root.right
      root.right = root.left
      root.left = None
      result = last
    last = self.preorderR(right)
    if last != None:
      result = last
    return result

  def preorderI(self, root):
    if root == None:
      return None
    stack, last = [root], None
    while len(stack) > 0:
      top = stack.pop()
      if top.right != None:
        stack.append(top.right)
      if top.left != None:
        stack.append(top.left)
      if last != None:
        last.left = None
        last.right = top
      last = top
