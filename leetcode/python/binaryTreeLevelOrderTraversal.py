# https://oj.leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return a list of lists of integers
  def levelOrder(self, root):
    if root == None:
      return []
    result, queue = [[root.val]], [[root]]
    while len(queue) > 0:
      curr = []
      for node in queue[0]:
        if node.left != None:
          curr.append(node.left)
        if node.right != None:
          curr.append(node.right)
      queue.pop(0)
      if len(curr) > 0:
        queue.append(curr)
        result.append([x.val for x in curr])
    return result

s = Solution()

print s.levelOrder(None)

root = TreeNode(1)
root.left = TreeNode(2)
print s.levelOrder(root)
