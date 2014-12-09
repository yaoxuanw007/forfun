# https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# 11:47 - 12:04

class Solution:
  # @return a ListNode
  def removeNthFromEnd(self, head, n):
    curr = head
    # move curr for n step
    for i in xrange(n):
      curr = curr.next
      if curr == None:
        break
    # If it's reach end, update head
    if curr == None:
      head = head.next
    # Otherwise, find the previous ListNode of the node to be removed
    else:
      last, curr = head, curr.next
      while curr != None:
        curr = curr.next
        last = last.next
      last.next = last.next.next
    return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
result = s.removeNthFromEnd(head, 2)
print result.val, 2

head = ListNode(1)
head.next = ListNode(2)
result = s.removeNthFromEnd(head, 1)
print result.val, 1
