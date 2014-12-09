# https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return an integer
  def sumNumbers(self, root):
    self.total = 0
    self.dfs(root, [])
    return self.total

  def dfs(self, root, path):
    if root == None:
      return
    path.append(root.val)
    if root.left == None and root.right == None:
      self.total += int(''.join([str(x) for x in path]))
    self.dfs(root.left, path)
    self.dfs(root.right, path)
    path.pop()

s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print s.sumNumbers(root)
