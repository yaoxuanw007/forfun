# https://oj.leetcode.com/problems/longest-consecutive-sequence/

O(n)
class Solution:
  # @param num, a list of integer
  # @return an integer
  def longestConsecutive(self, num):
    counts = {}
    longest = 0
    for i in num:
      # ignore duplicate integer
      if i not in counts:
        counts[i] = 1
        # use the start and end of interval to record the length of interval
        start = end = i
        # update counts[i] first
        if i-1 in counts:
          start = i - counts[i-1]
          counts[i] += counts[i-1]
        if i+1 in counts:
          end = i + counts[i+1]
          counts[i] += counts[i+1]
        # merge two intervals, then update
        counts[start] = counts[end] = counts[i]
        longest = max(counts[i], longest)
    return longest

s = Solution()

inputs = [
    [100, 200, 4, 1, 2, 3],
    [0,3,7,2,5,8,4,6,0,1]
    ]

for num in inputs:
  print s.longestConsecutive(num)
