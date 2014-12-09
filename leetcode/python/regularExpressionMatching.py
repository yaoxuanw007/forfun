# https://oj.leetcode.com/problems/regular-expression-matching/

class Solution:
  @classmethod
  def _memoize(cls, f):
    def helper(self, s, p):
      key = s + '|' + p
      if key not in self.memo:
        self.memo[key] = f(self, s, p)
      return self.memo[key]
    return helper

  def __init__(self):
    self.memo = {}

  def isMatch(self, s, p):
    self.memo.clear()
    return self.isMatchR(s, p)

  # @return a boolean
  def isMatchR(self, s, p):
    # If pattern string is empty
    if len(p) == 0:
      return len(s) == 0
    # If pattern has wildcard
    if len(p) >= 2 and '*' == p[1]:
      # Try current pattern: p[0:2] with 1/2/3/../len(s) charactors
      for i in xrange(1, len(s)+1):
        # If the first charactor s[i-1] doesn't match pattern,
        # skip this pattern
        if s[i-1] != p[0] and '.' != p[0]:
          break
        if self.isMatchR(s[i:], p[2:]):
          return True
      # Try next pattern
      return self.isMatchR(s, p[2:])
    else:
      # If string not is empty but pattern doesn't contain wildcard
      if len(s) > 0 and (s[0] == p[0] or '.' == p[0]):
        # move forward
        return self.isMatchR(s[1:], p[1:])
      return False

Solution.isMatchR = Solution._memoize(Solution.isMatchR)

# Test

solution = Solution()

inputs = [
    ("aa","a"),
    ("aa","aa"),
    ("aaa","aa"),
    ("aa", "a*"),
    ("aa", ".*"),
    ("ab", ".*"),
    ("aab", "c*a*b"),
    ("aaa", "a*a"),
    ("aaa", "a*a*a"),
    ("ab", "a*bb*"),
    ("aaa", "ab*a*c*a"),
    ("aba", "ab*a*c*a"),
    ("ab", ".*.."),
    ("a", ".*..a*"),
    ("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"),
    ]

for s,p in inputs:
  print solution.isMatch(s, p)
