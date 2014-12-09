# https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param preorder, a list of integers
  # @param inorder, a list of integers
  # @return a tree node
  def buildTree(self, preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
      return None
    return self.buildNode(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

  def buildNode(self, preorder, inorder, s1, e1, s2, e2):
    if s2 > e2:
      return None
    root = TreeNode(preorder[s1])
    rootIndex = inorder.index(preorder[s1])
    leftLen = rootIndex - s2
    root.left = self.buildNode(preorder, inorder, s1 + 1, s1 + leftLen, s2, rootIndex - 1)
    root.right = self.buildNode(preorder, inorder, s1 + leftLen + 1, e1, rootIndex + 1, e2)
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

root = s.buildTree([1,2,3], [3,2,1])
print s.preorderTree(root)
print s.levelTree(root)
