# https://oj.leetcode.com/problems/word-break/

class Solution:
  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  def wordBreak(self, s, dict):
    self.cache = {}
    return self.dfs(s, dict)

  # memorized dfs
  def dfs(self, s, dict):
    if len(s) == 0:
      return True
    if s in self.cache:
      return self.cache[s]
    for i in xrange(len(s), -1, -1):
      word = s[:i]
      if word in dict and self.dfs(s[i:], dict):
        self.cache[s] = True
        return True
    self.cache[s] = False
    return False

s = Solution()

print s.wordBreak("leetcode", ["leet", "code"])
