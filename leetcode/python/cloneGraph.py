# https://oj.leetcode.com/problems/clone-graph/

# Definition for a undirected graph node
class UndirectedGraphNode:
  def __init__(self, x):
    self.label = x
    self.neighbors = []

  def __repr__(self):
    return self.label + ':' + str(self.neighbors)

class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  def cloneGraph(self, node):
    if node == None:
      return None
    start, graph = node.label, self.traverse(node)
    return self.createNode(start, graph)

  def traverse(self, node):
    hasInQueue, queue, graph = set([node.label]), [node], {}
    while len(queue) > 0:
      front = queue.pop(0)
      fLabel = front.label
      if fLabel not in graph:
        graph[fLabel] = {
          'new': UndirectedGraphNode(fLabel),
          'neighbors': []
        }
      for neighbor in front.neighbors:
        nLabel = neighbor.label
        graph[fLabel]['neighbors'].append(nLabel)
        if nLabel not in hasInQueue:
          hasInQueue.add(nLabel)
          queue.append(neighbor)
    return graph

  def createNode(self, start, graph):
    for fLabel in graph.keys():
      for nLabel in graph[fLabel]['neighbors']:
        graph[fLabel]['new'].neighbors.append(graph[nLabel]['new'])
    return graph[start]['new']

# {0,1,5#1,2,5#2,3#3,4,4#4,5,5#5}

s = Solution()

print s.traverse(s.createNode('0', {
    '0': {'new': UndirectedGraphNode('0'), 'neighbors':['1','5']},
    '1': {'new': UndirectedGraphNode('1'), 'neighbors':['2','5']},
    '2': {'new': UndirectedGraphNode('2'), 'neighbors':['3']},
    '3': {'new': UndirectedGraphNode('3'), 'neighbors':['4','4']},
    '4': {'new': UndirectedGraphNode('4'), 'neighbors':['5','5']},
    '5': {'new': UndirectedGraphNode('5'), 'neighbors':[]}
    }))
