# https://oj.leetcode.com/problems/subsets/

class Solution:
  # @param S, a list of integer
  # @return a list of lists of integer
  def subsets(self, S):
    S = sorted(S)
    sLen = len(S)
    rLen = 2**sLen
    result = [[] for i in xrange(rLen)]
    for i in xrange(sLen):
      for j in xrange(rLen):
        if (j >> i) & 1:
          result[j].append(S[i])
    return result

s = Solution()

print s.subsets([1,2,3])
