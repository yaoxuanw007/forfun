# https://oj.leetcode.com/problems/copy-list-with-random-pointer/

class RandomListNode:
  def __init__(self, x):
    self.label = x
    self.next = None
    self.random = None

# O(n)
class Solution:
  # @param head, a RandomListNode
  # @return a RandomListNode
  def copyRandomList(self, head):
    if head == None:
      return None
    curr = head
    boxHead = None
    boxLast = None
    while curr != None:
      box = {
          'old': curr,
          'new': RandomListNode(curr.label),
          'random': curr.random,
          'next': None
          }
      if boxHead == None:
        boxHead = box
      if boxLast != None:
        boxLast['next'] = box
      boxLast = box
      # break the original link
      # use next of old node to store the new node
      next = curr.next
      curr.next = box['new']
      curr = next
    # set random
    boxCurr = boxHead
    while boxCurr != None:
      if boxCurr['random'] != None:
        boxCurr['new'].random = boxCurr['random'].next
      boxCurr = boxCurr['next']
    # chain old and new nodes
    boxCurr = boxHead
    boxLast = None
    while boxCurr != None:
      # clean next of old node
      boxCurr['old'].next = None
      # link new and old nodes
      if boxLast != None:
        boxLast['old'].next = boxCurr['old']
        boxLast['new'].next = boxCurr['new']
      boxLast = boxCurr
      boxCurr = boxCurr['next']
    return boxHead['new']

s = Solution()

head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)

head.next.next.random = head
head.next.random = None
head.random = head.next.next

curr = head
while curr != None:
  if curr.random != None:
    randomStr = str(curr.random.label)
  else:
    randomStr = '#'
  print str(curr.label) + '-' + randomStr
  curr = curr.next

copyHead = s.copyRandomList(head)
curr = copyHead
while curr != None:
  if curr.random != None:
    randomStr = str(curr.random.label)
  else:
    randomStr = '#'
  print str(curr.label) + '-' + randomStr
  curr = curr.next

curr = head
while curr != None:
  if curr.random != None:
    randomStr = str(curr.random.label)
  else:
    randomStr = '#'
  print str(curr.label) + '-' + randomStr
  curr = curr.next
