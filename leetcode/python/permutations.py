# https://oj.leetcode.com/problems/permutations/

class Solution:
  # @param num, a list of integer
  # @return a list of lists of integers
  def permute(self, num):
    result = [[]]
    for n in num:
      rLen = len(result)
      for i in xrange(rLen):
        x, j = result.pop(0), 0
        xLen = len(x)
        while j <= xLen:
          # handle duplicate element
          # if x[j] == n, it's same to insert before and after position j
          if j < xLen and x[j] == n:
            j += 1
            continue
          y = x[:]
          y.insert(j, n)
          result.append(y)
          j += 1
    return result

s = Solution()

print s.permute([1,2,3])
print s.permute([2,2,3])
