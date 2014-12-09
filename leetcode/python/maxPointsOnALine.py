# Question
#
# Given n points on a 2D plane, find the maximum number of points
# that lie on the same straight line.
#
# Link: https://oj.leetcode.com/problems/max-points-on-a-line/
class Point:
  def __init__(self, a=0, b=0):
    self.x = a
    self.y = b

  def __repr__(self):
    return str(self.x) + '|' + str(self.y)

# Ax + By + C = 0
# (0, 1) and (2, 2)
# => B + C = 0, 2A + 2B + C = 0 => A = C/2, B = -C => (C/2)x - Cy + C = 0 => x - 2y + 2 = 0
class Solution:
  # @param points, a list of Points
  # @return an integer
  def maxPoints(self, points):
    pLen = len(points)
    if pLen <= 2:
      return pLen
    result, hasFound = 0, []
    for i in xrange(pLen):
      if i in hasFound:
        continue
      lines, samePoints = {}, 1
      for j in xrange(i+1, pLen):
        if points[i].x == points[j].x:
          # Same point
          if points[i].y == points[j].y:
            samePoints += 1
            hasFound.append(j)
            continue
          # Vertical to x axis
          else:
            key = "1:0:" + str(-1*points[i].x)
        else:
          # Vertical to y axis
          if points[i].y == points[j].y:
            key = "0:1:" + str(-1*points[i].y)
          # Other lines
          else:
            a = 1
            # Cast to float
            b = -a*(points[i].x-points[j].x)*1.0/(points[i].y-points[j].y)
            c = -a*points[i].x - b*points[i].y
            key = str(a) + ':' + str(b) + ':' + str(c)
        # Include points[i]
        if key not in lines:
          lines[key] = 0
        # Include points[j]
        lines[key] += 1
      # Current point
      lines['-:-:-'] = 0
      for k in lines.keys():
        lines[k] += samePoints
        if lines[k] > result:
          result = lines[k]
      print lines
    return result

# Test
s = Solution()

print s.maxPoints([Point(0,0),Point(1,1),Point(1,-1)]), 2
print s.maxPoints([Point(1,1),Point(1,1),Point(1,1)]), 3
print s.maxPoints([Point(-4,-4),Point(-8,-582),Point(-3,3),Point(-9,-651),Point(9,591)]), 3
