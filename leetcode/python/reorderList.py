# https://oj.leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return nothing
  def reorderList(self, head):
    hLen, curr = 0, head
    # Get the length of list
    while curr != None:
      hLen += 1
      curr = curr.next
    # Split into two lists
    head1, head2 = head, head
    last = None
    for i in xrange(hLen / 2):
      last = head2
      head2 = head2.next
    if last != None:
      last.next = None
    # Reverse head2 list
    curr, last = head2, None
    while curr != None:
      next = curr.next
      curr.next = last
      last = curr
      curr = next
    if last != None:
      head2 = last
    # Merge two lists
    tail = None
    while head1 != None:
      next1, next2 = head1.next, head2.next
      if tail != None:
        tail.next = head1
      tail = head2
      head1.next = head2
      head2.next = None
      head1, head2 = next1, next2
    # Handle list with odd length
    if tail != None and head2 != None:
      tail.next = head2
    return head

  def printList(self, head):
    result, curr = [], head
    while curr != None:
      result.append(curr.val)
      curr = curr.next
    return result

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head = s.reorderList(head)
print s.printList(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head = s.reorderList(head)
print s.printList(head)

head = ListNode(1)
head = s.reorderList(head)
print s.printList(head)

head = s.reorderList(None)
print s.printList(head)
