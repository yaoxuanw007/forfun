# https://oj.leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param a list of ListNode
  # @return a ListNode
  def mergeKLists(self, lists):
    head, curr = None, None
    heap = [(x.val, x) for x in lists if x]
    heapq.heapify(heap)
    while len(heap) > 0:
      top = heapq.heappop(heap)
      if not head:
        head = top[1]
        curr = head
      else:
        curr.next = top[1]
        curr = curr.next
      next = top[1].next
      if next != None:
        heapq.heappush(heap, (next.val, next))
      curr.next = None
    return head
