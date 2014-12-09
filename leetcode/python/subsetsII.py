# https://oj.leetcode.com/problems/subsets-ii/

class Solution:
  # @param num, a list of integer
  # @return a list of lists of integer
  def subsetsWithDup(self, S):
    S = sorted(S)
    result, count = [[]], 0
    for i in xrange(len(S)):
      count += 1
      if i + 1 < len(S) and S[i] == S[i+1]:
        continue
      more, rLen = [], len(result)
      for j in xrange(count):
        more.append(S[i])
        result.extend([result[k] + more for k in xrange(rLen)])
      count = 0
    return result

s = Solution()

print s.subsetsWithDup([1,2,2])
