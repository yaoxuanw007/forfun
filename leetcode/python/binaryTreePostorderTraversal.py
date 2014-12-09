# https://oj.leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return a list of integers
  def postorderTraversal(self, root):
    result = []
    stack = [None]
    # left: process left child
    # right: process right child
    curr, left, right = root, True, True
    while curr != None:
      while left and curr.left != None:
        stack.insert(0, curr)
        curr = curr.left
        right = True
      if right and curr.right != None:
        stack.insert(0, curr)
        curr = curr.right
        left = True
      else:
        result.append(curr.val)
        if stack[0] != None:
          left = False
          if stack[0].left == curr:
            right = True
          else:
            right = False
        curr = stack.pop(0)
    return result

class Solution1:
  # @param root, a tree node
  # @return a list of integers
  def postorderTraversal(self, root):
    if root == None:
      return []

    result = []
    if root.left != None:
      result.extend(self.postorderTraversal(root.left))
    if root.right != None:
      result.extend(self.postorderTraversal(root.right))
    result.append(root.val)
    return result

s = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print s.postorderTraversal(root)

print s.postorderTraversal(None)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(2)
print s.postorderTraversal(root)

root = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(2)
print s.postorderTraversal(root)
