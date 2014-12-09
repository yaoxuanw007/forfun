# https://oj.leetcode.com/problems/path-sum/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# DFS
class Solution:
  # @param root, a tree node
  # @param sum, an integer
  # @return a boolean
  def hasPathSum(self, root, sum):
    return self.isPathSumEqual(root, 0, sum)

  def isPathSumEqual(self, root, currSum, targetSum):
    if root == None:
      return False

    # make sure it's leaf
    currSum += root.val
    if root.left == None and root.right == None:
      return currSum == targetSum
    return self.isPathSumEqual(root.left, currSum, targetSum) or \
        self.isPathSumEqual(root.right, currSum, targetSum)

s = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print s.hasPathSum(root, 22)
print s.hasPathSum(root, 21)
print s.hasPathSum(None, 0)

root = TreeNode(1)
root.left = TreeNode(2)

print s.hasPathSum(root, 1)
