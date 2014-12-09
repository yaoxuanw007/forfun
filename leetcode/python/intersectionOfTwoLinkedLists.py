# https://oj.leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# time: O(m+n); space: O(1)
class Solution:
  # @param two ListNodes
  # @return the intersected ListNode
  def getIntersectionNode(self, headA, headB):
    m, n = 0, 0
    curr = headA
    while curr != None:
      curr = curr.next
      m += 1
    curr = headB
    while curr != None:
      curr = curr.next
      n += 1

    sizeDiff = abs(m - n)
    if m > n:
      for i in xrange(sizeDiff):
        headA = headA.next
    else:
      for i in xrange(sizeDiff):
        headB = headB.next

    while headA != None:
      if headA == headB:
        return headA
      headA = headA.next
      headB = headB.next
    return None
