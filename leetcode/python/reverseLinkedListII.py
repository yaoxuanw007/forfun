# https://oj.leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @param m, an integer
  # @param n, an integer
  # @return a ListNode
  def reverseBetween(self, head, m, n):
    last, curr = None, head
    for i in xrange(m-1):
      last = curr
      curr = curr.next
    tail = curr
    for i in xrange(n-m+1):
      next = curr.next
      if last != None:
        curr.next = last.next
        last.next = curr
      else:
        curr.next = head
        head = curr
      curr = next
    tail.next = curr
    return head
