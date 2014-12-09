# https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a binary tree node
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
      return

    queue = [root]
    while len(queue) > 0:
      num = len(queue)
      last = None
      while num > 0:
        curr = queue.pop(0)
        if last != None:
          last.next = curr
        last = curr
        if curr.left != None:
          queue.append(curr.left)
        if curr.right != None:
          queue.append(curr.right)
        num -= 1
