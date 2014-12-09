# https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return a list of lists of integers
  def zigzagLevelOrder(self, root):
    if root == None:
      return []
    result, queue, leftToRight = [], [root], True
    while len(queue) > 0:
      qLen, level = len(queue), []
      for i in xrange(qLen):
        top = queue.pop(0)
        if top.left != None:
          queue.append(top.left)
        if top.right != None:
          queue.append(top.right)
        if leftToRight:
          level.append(top.val)
        else:
          level.insert(0, top.val)
      leftToRight = not leftToRight
      result.append(level)
    return result

s= Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print s.zigzagLevelOrder(root)
