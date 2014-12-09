# https://oj.leetcode.com/problems/word-ladder/

import heapq

class Solution:
  # @param start, a string
  # @param end, a string
  # @param dict, a set of string
  # @return an integer
  def ladderLength(self, start, end, dict):

    # BFS2
    self.minLen = self.bfs2(start, end, dict)

    # DFS
    # self.minLen = 0
    # self.createGraph(start, end, dict)
    # self.dfs(end, start, [])

    # BFS
    # self.createGraph(start, end, dict)
    # self.minLen = self.bfs(start, end)

    # dijkstra
    # self.createGraph(start, end, dict)
    # self.minLen = self.dijkstra(start, end)

    return self.minLen

  def createGraph(self, start, end, dict):
    words = list(dict) + [start, end]
    self.graph = {}
    for w1 in words:
      self.graph[w1] = []
      for w2 in words:
        if w1 != w2 and self.hasOneDiff(w1, w2):
          self.graph[w1].append(w2)

  def hasOneDiff(self, w1, w2):
    num = 0
    for i in xrange(len(w1)):
      if w1[i] != w2[i]:
        num += 1
    return num == 1

  # Pass OJ!!
  # Don't generate graph
  def bfs2(self, start, end, dict):
    letters = [chr(x) for x in xrange(ord('a'), ord('z')+1)]
    dis, queue = {start: 1}, [start]
    while len(queue) > 0:
      top = queue.pop(0)
      for i in xrange(len(top)):
        for c in letters:
          word = top[:i] + c + top[i+1:]
          if word == top:
            continue
          if word == end:
            return dis[top] + 1
          if word in dict:
            if word not in dis:
              dis[word] = 0
            if dis[word] == 0:
              dis[word] = dis[top] + 1
              queue.append(word)
    return 0

  # TLE
  def dijkstra(self, start, end):
    visited, heap = [], [(0, start)]
    heapq.heapify(heap)
    while len(heap) > 0:
      top = heapq.heappop(heap)
      adjacents = self.graph[top[1]]
      if end in adjacents:
        return top[0] + 1
      for s in adjacents:
        if s not in visited:
          heapq.heappush(heap, (top[0] + 1, s))
      visited.append(top[1])
    return -1

  # TLE
  def bfs(self, start, end):
    queue, visited = [(start, 0)], set()
    while len(queue) > 0:
      top = queue.pop(0)
      children = self.graph[top[0]]
      if end in children:
        return top[1]+1
      queue.extend([(x, top[1]+1) for x in children if x not in visited])
      visited.add(top[0])
    return -1

  # TLE
  def dfs(self, end, curr, path):
    if self.minLen > 0 and len(path) >= self.minLen:
      return
    if curr in path:
      return

    path.append(curr)
    children = self.graph[curr]
    if end in children:
      self.minLen = len(path) + 1
    else:
      for child in children:
        self.dfs(end, child, path)
    path.pop()

s = Solution()

print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print s.ladderLength("hot", "dog", ["hot","dog"])
