# https://oj.leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# 16:50 - 17:01

# Assume that the lists are ascending
class Solution:
  # @param two ListNodes
  # @return a ListNode
  def mergeTwoLists(self, l1, l2):
    curr1, curr2, head, last, curr = l1, l2, None, None, None
    while curr1 != None or curr2 != None:
      if curr1 != None and curr2 != None:
        if curr1.val < curr2.val:
          curr = curr1
          curr1 = curr1.next
        else:
          curr = curr2
          curr2 = curr2.next
      elif curr1 != None:
        curr = curr1
        curr1 = None
      else:
        curr = curr2
        curr2 = None
      if head == None:
        head = curr
      if last != None:
        last.next = curr
      last = curr
    return head

s = Solution()

l1 = ListNode(1)
l1.next = ListNode(3)
l2 = ListNode(2)
curr = s.mergeTwoLists(l1, l2)
while curr != None:
  print curr.val
  curr = curr.next
print

l1 = None
l2 = ListNode(2)
curr = s.mergeTwoLists(l1, l2)
while curr != None:
  print curr.val
  curr = curr.next
print

l1 = ListNode(1)
l2 = None
curr = s.mergeTwoLists(l1, l2)
while curr != None:
  print curr.val
  curr = curr.next
print

