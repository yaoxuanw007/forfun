# Link: https://oj.leetcode.com/problems/trapping-rain-water/

# [0,1,0,2,1,0,1,3,2,1,2,1]
#
# =>
#
# [0,0,0,0,0,0,0,1,0,0,0,0]
# [0,0,0,1,0,0,0,1,1,0,1,0]
# [0,1,0,1,1,0,1,1,1,1,1,1]

# O(n)
class Solution:
  # @param A, a list of integers
  # @return an integer
  def trap(self, A):
    sum, last, stack, counts, first = 0, 0, [], [], False
    for i in A:
      if not first:
        if i > 0:
          first = True
          stack.insert(0, i)
          counts.insert(0, 1)
          last = i
      else:
        if stack[0] >= i:
          stack.insert(0, i)
          counts.insert(0, 1)
        else:
          count = 1
          while stack[0] < i:
            if stack[0] == last:
              break
            # last is another border
            sum += (min(i, last) - stack.pop(0)) * counts[0]
            count += counts.pop(0)
          stack.insert(0, i)
          counts.insert(0, count)
          # last max value
          if i > last:
            last = i
      # print str(stack) + " - " + str(counts) + " - " + str(sum)
    return sum


# O(n*h)
class Solution1:
  # @param A, a list of integers
  # @return an integer
  def trap(self, A):
    sumVal = 0
    while True:
      minVal, count, first = -1, 0, False
      for v in A:
        if v > 0:
          if minVal > v:
            minVal = v
          elif minVal < 0:
            minVal = v
      for i in xrange(0, len(A)):
        if A[i] > 0 and not first:
          first = True
        elif first:
          if A[i] == 0:
            count += 1
          else:
            sumVal += count*minVal
            count = 0
        if A[i] > 0:
          A[i] -= minVal
      if not first:
        break
    return sumVal

s = Solution()

nums = [
   [0,1,0,2,1,0,1,3,2,1,2,1],
   [0,1,0],
   [0,1,3],
   [1,0,1],
   [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
    ]

for num in nums:
  print s.trap(num)
