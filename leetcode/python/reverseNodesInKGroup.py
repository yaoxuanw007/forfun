# https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @param k, an integer
  # @return a ListNode
  def reverseKGroup(self, head, k):
    curr, tail = head, None
    while curr != None:
      pHead, hasK = None, True
      # find head and tail
      for i in xrange(k):
        if i == 0:
          pHead = curr
        if not curr:
          hasK = False
          break
        curr = curr.next
      # If hasK == False, the left-out nodes is less than k.
      # Otherwise, reverse list
      pTail = None
      if hasK:
        pCurr = pHead
        pHead = None
        for i in xrange(k):
          pNext = pCurr.next
          if i == 0:
            pTail = pCurr
          pCurr.next = pHead
          pHead = pCurr
          pCurr = pNext
      # Link two parts
      if tail:
        tail.next = pHead
      else:
        head = pHead
      # Store the tail of last part
      tail = pTail
    return head

