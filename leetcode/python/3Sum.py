# https://oj.leetcode.com/problems/3sum/

class Solution:
  # @return a list of lists of length 3, [[val1,val2,val3]]
  def threeSum(self, num):
    result = []
    num = self.sorted(num)
    nLen, i = len(num), 0
    while i < nLen - 2:
      j, k = i + 1, nLen - 1
      while j < k:
        total = sum([num[i], num[j], num[k]])
        if total == 0:
          result.append([num[i], num[j], num[k]])
          # remove all duplicate
          while j < k and num[j] == num[j+1]:
            j += 1
          while j < k and num[k] == num[k-1]:
            k -= 1
          j += 1
          k -= 1
        elif total < 0:
          # remove all duplicate
          while j < k and num[j] == num[j+1]:
            j += 1
          j += 1
        else:
          # remove all duplicate
          while j < k and num[k] == num[k-1]:
            k -= 1
          k -= 1
      # remove all duplicate
      while i < nLen - 2 and num[i] == num[i+1]:
        i += 1
      i += 1
    return result

  # remove unnecessary elements
  def sorted(self, num):
    result, map = [], {}
    for n in num:
      if n not in map:
        map[n] = 1
      else:
        map[n] += 1
    for n in sorted(map.keys()):
      if map[n] >= 2:
        if n == 0 and map[n] >= 3:
          count = 3
        else:
          count = 2
      else:
        count = map[n]
      for i in xrange(count):
        result.append(n)
    return result


s = Solution()

print s.threeSum([-1,0,1,2,-1,-4])
print s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
print s.threeSum([0,0,0,0,0,0])
print s.threeSum([0,0])
print s.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])
