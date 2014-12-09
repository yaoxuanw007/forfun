# https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    self.next = None

class Solution:
  # @param root, a tree node
  # @return nothing
  def connect(self, root):
    if root == None:
      return None
    currLevel = [root]
    while len(currLevel) > 0:
      nextLevel, last = [], None
      for node in currLevel:
        if node.left != None:
          nextLevel.append(node.left)
        if node.right != None:
          nextLevel.append(node.right)
        if last != None:
          last.next = node
        last = node
      currLevel = nextLevel
