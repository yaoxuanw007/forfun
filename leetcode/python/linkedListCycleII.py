# https://oj.leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return a list node
  # no extra space
  def detectCycle(self, head):
    while head != None:
      if head.val == None:
        return head
      head.val = None
      head = head.next
    return None

  # O(1) space
  def detectCycle1(self, head):
    pos1, pos2 = head, head
    while pos1 != None and pos1.next != None:
      pos1 = pos1.next.next
      pos2 = pos2.next
      if pos1 == pos2:
        pos2 = head
        while pos1 != pos2:
          pos1 = pos1.next
          pos2 = pos2.next
        return pos1
    return None
