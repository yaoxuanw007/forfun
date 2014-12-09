# https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return a list of integers
  def inorderTraversal(self, root):
    # return self.inorderR(root)
    return self.inorderI(root)

  def inorderR(self, root):
    if root == None:
      return []
    left = self.inorderR(root.left)
    right = self.inorderR(root.right)
    return left + [root.val] + right

  def inorderI(self, root):
    if root == None:
      return []
    # stack: [node, toCheckRight]
    result, stack = [], [[root, False]]
    while len(stack) > 0:
      top = stack[-1]
      if not top[1]:
        if top[0].left != None:
          stack.append([top[0].left, False])
        top[1] = True
      else:
        result.append(top[0].val)
        stack.pop(-1)
        if top[0].right != None:
          stack.append([top[0].right, False])
    return result

s = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print s.inorderTraversal(root)
