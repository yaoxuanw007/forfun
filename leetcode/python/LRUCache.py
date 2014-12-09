class LRUCache:
  # @param capacity, an integer
  def __init__(self, capacity):
    self.time = 0
    self.map = {}
    self.heap = []
    self.count = 0
    self.capacity = capacity

  def heapmovedown(self, i):
    while True:
      left, right, min = 2*i+1, 2*i+2, i
      if left >= self.count:
        break
      # get min
      if left < self.count and self.heap[left][0] < self.heap[i][0]:
        min = left
      # if right is min
      if right < self.count and self.heap[right][0] < self.heap[min][0]:
        self.trackswap(right, i)
        i = right
      # if left is min
      elif min == left:
        self.trackswap(left, i)
        i = left
      # if i is min, finish
      else:
        break
    return i

  def heapmoveup(self, i):
    while True:
      if i == 0:
        break
      parent = (i-1)/2
      if self.heap[parent][0] <= self.heap[i][0]:
        break
      self.trackswap(parent, i)
      i = parent
    return i

  def trackswap(self, i, j):
    # track new index
    self.map[self.heap[i][1]] = j
    # swap
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def heappush(self, key, value):
    if self.count >= self.capacity:
      del self.map[self.heap[0][1]]
      self.heap[0] = [self.now(), key, value]
      return self.heapmovedown(0)
    else:
      self.count += 1
      self.heap.append([self.now(), key, value])
      return self.heapmoveup(self.count-1)

  # @return an integer
  def get(self, key):
    if key not in self.map:
      return -1
    else:
      i = self.map[key]
      value = self.heap[i][2]
      self.heap[i][0] = self.now()
      self.map[key] = self.heapmovedown(i)
    print self.heap
    return value

  # @param key, an integer
  # @param value, an integer
  # @return nothing
  def set(self, key, value):
    if key in self.map:
      i = self.map[key]
      self.heap[i] = [self.now(), key, value]
      self.map[key] = self.heapmovedown(i)
    else:
      self.map[key] = self.heappush(key, value)
    print self.heap

  def now(self):
    self.time += 1
    return self.time

# Test

c = LRUCache(10)

# c.set('a', 10)
# c.set('b', 20)
# print c.get('a')
# print c.get('a')
# print c.get('b')
# c.set('c', 30)
# print c.get('b')
# print c.get('c')

# c.set(2,1)
# c.set(2,2)
# print c.get(2)
# c.set(1,1)
# c.set(4,1)
# print c.get(2)

# c.set(2,1)
# c.set(1,1)
# print c.get(2)
# c.set(4,1)
# print c.get(1)
# print c.get(2)

c.set(10,13)
c.set(3,17)
c.set(6,11)
c.set(10,5)
c.set(9,10)
print c.get(13)
c.set(2,19)
print c.get(2)
print c.get(3)
c.set(5,25)
print c.get(8)
c.set(9,22)
c.set(5,5)
c.set(1,30)
print c.get(11)
c.set(9,12)
print c.get(7)
print c.get(5)
print c.get(8)
print c.get(9)
c.set(4,30)
c.set(9,3)
print c.get(9)
print c.get(10)
print c.get(10)
c.set(6,14)
c.set(3,1)
print c.get(3)
c.set(10,11)
print c.get(8)
c.set(2,14)
print c.get(1)
print c.get(5)
print c.get(4)
c.set(11,46)
print c.get(1)
c.set(12,17)
c.set(9,1)
c.set(6,19)
print c.get(4)
print c.get(5)
print c.get(5)
c.set(8,1)
c.set(11,7)
c.set(5,2)
c.set(9,28)
print c.get(1)
c.set(2,2)
c.set(7,4)
c.set(4,22)
c.set(7,24)
c.set(9,26)
c.set(13,28)
c.set(11,26)

