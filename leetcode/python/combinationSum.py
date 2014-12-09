# https://oj.leetcode.com/problems/combination-sum/

class Solution:
  # @param candidates, a list of integers
  # @param target, integer
  # @return a list of lists of integers
  def combinationSum(self, candidates, target):
    self.result = []
    candidates = sorted(candidates, reverse=True)
    self.combination(candidates, 0, [], target)
    return self.result

  def combination(self, candidates, pos, comb, target):
    cLen = len(candidates)
    if pos >= cLen:
      return

    comb.insert(0, candidates[pos])
    combSum = sum(comb)
    if combSum == target:
      self.result.append(comb[:])
    elif combSum < target:
      # try current pos again
      self.combination(candidates, pos, comb, target)
    comb.pop(0)

    while pos < cLen - 1 and candidates[pos+1] == candidates[pos]:
      pos += 1
    self.combination(candidates, pos+1, comb, target)

s = Solution()

print s.combinationSum([2,3,6,7], 7)
