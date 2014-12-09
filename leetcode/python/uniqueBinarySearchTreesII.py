# https://oj.leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @return a list of tree node
  def generateTrees(self, n):
    if n == 0:
      return [None]
    return self.generate(range(1, n+1))

  def generate(self, A):
    result = []
    if len(A) == 1:
      result.append(TreeNode(A[0]))
    else:
      for i in xrange(len(A)):
        lefts, rights = [], []
        if i > 0:
          lefts = self.generate(A[:i])
        if i < len(A) - 1:
          rights = self.generate(A[i+1:])
        if i == 0:
          for r in rights:
            root = TreeNode(A[i])
            root.right = r
            result.append(root)
        elif i == len(A) - 1:
          for l in lefts:
            root = TreeNode(A[i])
            root.left = l
            result.append(root)
        else:
          for l in lefts:
            for r in rights:
              root = TreeNode(A[i])
              root.left = l
              root.right = r
              result.append(root)
    return result

s = Solution()

print s.generateTrees(3)
