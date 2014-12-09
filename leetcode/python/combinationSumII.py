# https://oj.leetcode.com/problems/combination-sum-ii/

class Solution:
  # @param candidates, a list of integers
  # @param target, integer
  # @return a list of lists of integers
  def combinationSum2(self, candidates, target):
    self.result = []
    # sort in desending order
    # O(nlogn)
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
    # skip some branches
    elif combSum <= target:
      self.combination(candidates, pos+1, comb, target)
    comb.pop(0)

    # skip same element
    while pos < cLen - 1 and candidates[pos+1] == candidates[pos]:
      pos += 1
    self.combination(candidates, pos+1, comb, target)

s = Solution()

print s.combinationSum2([10,1,2,7,6,1,5], 8)
print s.combinationSum2([], 8)
