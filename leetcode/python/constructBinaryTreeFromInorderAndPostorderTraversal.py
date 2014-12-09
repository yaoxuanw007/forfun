# https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param inorder, a list of integers
  # @param postorder, a list of integers
  # @return a tree node
  def buildTree(self, inorder, postorder):
    if len(inorder) == 0 or len(postorder) == 0 or len(inorder) != len(postorder):
      return None
    return self.buildNode(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

  def buildNode(self, inorder, postorder, s1, e1, s2, e2):
    if s1 > e1:
      return None
    root = TreeNode(postorder[e2])
    rootIndex = inorder.index(postorder[e2])
    leftLen = rootIndex - s1
    root.left = self.buildNode(inorder, postorder, s1, rootIndex - 1, s2, s2 + leftLen - 1)
    root.right = self.buildNode(inorder, postorder, rootIndex + 1, e1, s2 + leftLen, e2 - 1)
    return root

  def preorderTree(self, root):
    if root == None:
      return ['#']
    left = self.preorderTree(root.left)
    right = self.preorderTree(root.right)
    return [str(root.val)] + left + right

  def levelTree(self, root):
    result, queue = [], [root]
    while len(queue) > 0:
      level = []
      for i in xrange(len(queue)):
        top = queue.pop(0)
        if top != None:
          level.append(top.val)
          queue.append(top.left)
          queue.append(top.right)
        else:
          level.append('#')
      result.append(level)
    return result

s = Solution()

root = s.buildTree([1,2], [1,2])
print s.preorderTree(root)
print s.levelTree(root)
