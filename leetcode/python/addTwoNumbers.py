# https://oj.leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    head, tail, curr, carry = None, None, None, 0
    while l1 != None or l2 != None:
      if l1 != None and l2 != None:
        carry += l1.val + l2.val
        l1, l2 = l1.next, l2.next
      elif l1 != None:
        carry += l1.val
        l1 = l1.next
      else:
        carry += l2.val
        l2 = l2.next
      curr = ListNode(carry % 10)
      carry /= 10
      if head == None:
        head = curr
      if tail != None:
        tail.next = curr
      tail = curr
    if carry > 0:
      tail.next = ListNode(carry)
    return head

s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

head = s.addTwoNumbers(l1,l2)

while head != None:
  print head.val
  head = head.next
print
