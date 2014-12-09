# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return a ListNode
  def deleteDuplicates(self, head):
    last, curr, dup = None, head, False
    while curr != None:
      if curr.next and curr.val == curr.next.val:
        if not dup:
          dup = True
        if not last:
          head = curr.next
        else:
          last.next = curr.next
      elif dup:
        # remove last element if duplicated
        dup = False
        if not last:
          head = curr.next
        else:
          last.next = curr.next
      else:
        last = curr
      curr = curr.next
    return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
head = s.deleteDuplicates(head)

result, curr = [], head
while curr != None:
  result.append(curr.val)
  curr = curr.next
print result


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head = s.deleteDuplicates(head)

result, curr = [], head
while curr != None:
  result.append(curr.val)
  curr = curr.next
print result
