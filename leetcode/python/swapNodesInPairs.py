# https://oj.leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param a ListNode
  # @return a ListNode
  def swapPairs(self, head):
    curr, tail = head, None
    while curr:
      pHead = curr
      pTail = pNext = curr.next
      # If there are two nodes
      if pTail:
        pNext = pTail.next
        pTail.next = pHead
        pHead.next = pNext
        pHead, pTail = pTail, pHead
      # Link two lists
      if tail:
        tail.next = pHead
      else:
        head = pHead
      # Store the tail of last pair
      tail = pTail
      curr = pNext
    return head
