# https://oj.leetcode.com/problems/merge-intervals/

# Definition for an interval.
class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

  def __repr__(self):
    return str([self.start, self.end])

class Solution:
  # @param intervals, a list of Interval
  # @return a list of Interval
  def merge(self, intervals):
    result = []
    iLen = len(intervals)
    if iLen > 0:
      # O(nlogn)
      sortedIntervals = sorted(intervals, key=lambda x: x.start);
      # O(n)
      start, end = sortedIntervals[0].start, sortedIntervals[0].end
      for i in xrange(1, iLen):
        # if new end is larger than the merged end
        if sortedIntervals[i].start <= end and sortedIntervals[i].end > end:
          end = sortedIntervals[i].end
        # if no overlap with the merged interval
        elif sortedIntervals[i].start > end:
          result.append(Interval(start, end))
          start = sortedIntervals[i].start
          end = sortedIntervals[i].end

      result.append(Interval(start, end))

    return result

s = Solution()

print s.merge([Interval(x, y) for x,y in [[1,3],[2,6],[8,10],[15,18]]])
