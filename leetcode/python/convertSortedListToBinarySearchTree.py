# https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a list node
  # @return a tree node
  def sortedListToBST(self, head):
    num, curr = 0, head
    while curr != None:
      num += 1
      curr = curr.next
    return self.listToBST(head, num)

  def listToBST(self, head, num):
    root = None
    if num > 0:
      # find mid value
      curr = head
      for i in xrange(num / 2):
        curr = curr.next
      root = TreeNode(curr.val)
      root.left = self.listToBST(head, num/2)
      # this will take care of integer division
      root.right = self.listToBST(curr.next, num - num/2 - 1)
    return root
