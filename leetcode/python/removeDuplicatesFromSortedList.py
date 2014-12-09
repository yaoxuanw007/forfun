# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# 12:14 - 12:24

class Solution:
  # @param head, a ListNode
  # @return a ListNode
  def deleteDuplicates(self, head):
    hasFound = {}
    last, curr = head, head
    while curr != None:
      if curr.val in hasFound:
        last.next = curr.next
        # don't need to update last
        curr = curr.next
        continue
      else:
        hasFound[curr.val] = 1
      last = curr
      curr = curr.next
    return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
node = s.deleteDuplicates(head)
while node != None:
  print node.val
  node = node.next
print

head = ListNode(1)
head.next = ListNode(1)
head.next = ListNode(1)
node = s.deleteDuplicates(head)
while node != None:
  print node.val
  node = node.next
print

head = ListNode(1)
node = s.deleteDuplicates(head)
while node != None:
  print node.val
  node = node.next
print

head = ListNode(None)
node = s.deleteDuplicates(head)
while node != None:
  print node.val
  node = node.next
print
