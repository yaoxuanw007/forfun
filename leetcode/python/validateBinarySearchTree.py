# https://oj.leetcode.com/problems/validate-binary-search-tree/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return a boolean
  def isValidBST(self, root):
    if root == None:
      return True
    result = self.isValid(root)
    return result[0]

  def isValid(self, root):
    valid, minVal, maxVal = True, root.val, root.val
    if root.left != None:
      leftValid, leftMinVal, leftMaxVal = self.isValid(root.left)
      valid = leftValid and leftMaxVal < root.val
      minVal = leftMinVal
    if valid and root.right != None:
      rightValid, rightMinVal, rightMaxVal = self.isValid(root.right)
      valid = rightValid and rightMinVal > root.val
      maxVal = rightMaxVal
    return [valid, minVal, maxVal]

s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print s.isValidBST(root)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print s.isValidBST(root)
