# https://oj.leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return a boolean
  # O(n), no extra space
  def hasCycle(self, head):
    while head != None:
      if head.val == None:
        return True
      head.val = None
      head = head.next
    return False

  # Space: O(1)
  def hasCycle1(self, head):
    fast, slow = head, head
    while fast != None and fast.next != None:
      fast = fast.next.next
      slow = slow.next
      if slow == fast:
        return True
    return False

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next
print s.hasCycle(head)
print s.hasCycle1(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print s.hasCycle(head)
print s.hasCycle1(head)

head = ListNode(1)
head.next = head
print s.hasCycle(head)
print s.hasCycle1(head)
