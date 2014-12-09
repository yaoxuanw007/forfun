# https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# 10:44 - 11:00

class Solution:
  # @param root, a tree node
  # @return a list of lists of integers
  def levelOrderBottom(self, root):
    if root == None:
      return []
    result, queue = [[root.val]], [[root]]
    while len(queue) > 0:
      next = []
      for node in queue[0]:
        if node.left != None:
          next.append(node.left)
        if node.right != None:
          next.append(node.right)
      queue.pop(0)
      if len(next) > 0:
        queue.append(next)
        result.insert(0, [x.val for x in next])
    return result

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print str([str(x) for x in s.levelOrderBottom(root)])
