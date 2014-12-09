# https://oj.leetcode.com/problems/anagrams/

class Solution:
  # @param strs, a list of strings
  # @return a list of strings
  def anagrams(self, strs):
    result, anagrams = [], {}
    for s in strs:
      key = self.getKey(s)
      if key not in anagrams:
        anagrams[key] = []
      anagrams[key].append(s)
    for k in anagrams.keys():
      if len(anagrams[k]) > 1:
        result.extend(anagrams[k])
    return result

  def getKey(self, s):
    counts = {}
    for c in s:
      if c not in counts:
        counts[c] = 0
      counts[c] += 1
    result = ""
    for k in sorted(counts.keys()):
      result += k + str(counts[k])
    return result
