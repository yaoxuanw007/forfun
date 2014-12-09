# https://oj.leetcode.com/problems/insert-interval/

# Definition for an interval.
class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

  def __repr__(self):
    return str([self.start, self.end])

class Solution:
  # @param intervals, a list of Intervals
  # @param newInterval, a Interval
  # @return a list of Interval
  def insert(self, intervals, newInterval):

    first, second = [], []
    start, end = newInterval.start, newInterval.end
    for interval in intervals:
      # skip, if covered by merged newInterval
      if interval.start >= start and interval.end <= end:
        continue

      # update start if there is overlap
      if interval.end >= start and interval.start < start:
        start = interval.start
      # update end
      if interval.start <= end and interval.end > end:
        end = interval.end

      # prepare first and second part separately
      if interval.end < start:
        first.append(interval)
      elif interval.start > end:
        second.append(interval)

    return first + [Interval(start, end)] + second

s = Solution()

print s.insert([Interval(x,y) for x,y in [[1,2],[3,5],[6,7],[8,10],[12,16]]], Interval(4,9))
print s.insert([Interval(x,y) for x,y in [[1,3],[6,9]]], Interval(2,5))
print s.insert([Interval(x,y) for x,y in [[1,5]]], Interval(5,7))
