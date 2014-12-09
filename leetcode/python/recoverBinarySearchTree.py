# https://oj.leetcode.com/problems/recover-binary-search-tree/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
  self.val = x
  self.left = None
  self.right = None

class Solution:
  # @param root, a tree node
  # @return a tree node
  def recoverTree(self, root):
    if root == None:
      return None

    self.nodes = []
    self.traverse(root)

    last = self.nodes[0]
    prev, next = None, None
    for curr in self.nodes:
      if last != None and last.val > curr.val:
        if prev == None:
          prev = last
        # get the last reverse pair
        next = curr
      last = curr
    tmp = prev.val
    prev.val = next.val
    next.val = tmp

    return root

  def traverse(self, root):
    if root.left != None:
      self.traverse(root.left)
    self.nodes.append(root)
    if root.right != None:
      self.traverse(root.right)


