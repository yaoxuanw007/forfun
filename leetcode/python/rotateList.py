# https://oj.leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @param k, an integer
  # @return a ListNode
  def rotateRight(self, head, k):
    if head == None:
      return None
    curr, hLen = head, 0
    # O(n)
    while curr != None:
      hLen += 1
      curr = curr.next
    k %= hLen
    if k == 0:
      return head
    # O(n)
    # rotate the list to the right by k places
    # i.e. rotate the list to the left of (hLen - k) places
    k = hLen - k
    curr = head
    for i in xrange(k):
      last = curr
      curr = curr.next
    tail = curr
    while tail.next != None:
      tail = tail.next
    last.next = None
    tail.next = head
    head = curr
    return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

curr = s.rotateRight(head, 2)
while curr != None:
  print curr.val
  curr = curr.next
