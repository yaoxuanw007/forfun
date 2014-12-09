# https://oj.leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @param x, an integer
  # @return a ListNode
  def partition(self, head, x):
    sHead, sTail = None, None
    curr, last = head, None
    while curr != None:
      if curr.val < x:
        if not sHead:
          sHead = curr
          sTail = sHead
        else:
          sTail.next = curr
          sTail = sTail.next
        # remove curr from list
        # and don't change last
        if last != None:
          last.next = curr.next
        # change head for the rest of list
        if head == curr:
          head = curr.next
      else:
        last = curr
      curr = curr.next
    if sTail != None:
      sTail.next = head
      head = sHead
    return head

s = Solution()

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
head = s.partition(head, 3)

result, curr = [], head
while curr != None:
  result.append(curr.val)
  curr = curr.next
print result
