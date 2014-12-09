# https://oj.leetcode.com/problems/path-sum-ii/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @param sum, an integer
  # @return a list of lists of integers
  def pathSum(self, root, sum):
    self.result = []
    self.dfs(root, [], sum)
    return self.result

  def dfs(self, root, path, target):
    if root == None:
      return
    path.append(root.val)
    if root.left == None and root.right == None:
      if sum(path) == target:
        self.result.append(path[:])
    self.dfs(root.left, path, target)
    self.dfs(root.right, path, target)
    path.pop()

s = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print s.pathSum(root, 22)
