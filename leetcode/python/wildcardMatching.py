# https://oj.leetcode.com/problems/wildcard-matching/

class Solution:
  @classmethod
  def _memorize(cls, f):
    def helper(self, s, p):
      key = s + '|' + p
      if key not in self.memo:
        self.memo[key] = f(self, s, p)
      return self.memo[key]
    return helper

  def __init__(self):
    self.memo = {}

  # Time Limit Excess
  # def isMatch(self, s, p):
  #   self.memo.clear()
  #   return self.isMatchR(s, p)

  # credit: http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
  def isMatch(self, s, p):
    sLen, pLen = len(s), len(p)
    sCurr, pCurr = 0, 0
    sMatch, pStar = -1, -1
    while sCurr < sLen:
      if pCurr < pLen and (s[sCurr] == p[pCurr] or p[pCurr] == '?'):
        sCurr += 1
        pCurr += 1
      elif pCurr < pLen and p[pCurr] == '*':
        # match 0 charactors for this '*'
        # pStar: the index of last '*' in pattern
        # sMatch: the next index in s to match last '*'
        sMatch = sCurr
        pStar = pCurr
        pCurr += 1
      elif pStar >= 0:
        # try to match from last '*' again
        # and match one more charactor for last '*'
        pCurr = pStar + 1
        sMatch += 1
        sCurr = sMatch
      else:
        # if no * is found
        return False
    # only '*' match empty string
    while pCurr < pLen and p[pCurr] == '*':
      pCurr += 1
    if pCurr == pLen:
      return True
    return False

  # @param s, an input string
  # @param p, a pattern string
  # @return a boolean
  def isMatchR(self, s, p):
    if len(p) == 0:
      return len(s) == 0
    if len(p) >= 1 and p[0] == '*':
      for i in xrange(1,len(s)+1):
        if self.isMatchR(s[i:], p[1:]):
          return True
      return self.isMatchR(s, p[1:])
    else:
      if len(s) > 0 and (s[0] == p[0] or p[0] == '?'):
        return self.isMatchR(s[1:], p[1:])
      return False

Solution.isMatchR = Solution._memorize(Solution.isMatchR)

# Test

s = Solution()

print s.isMatch("aa","a"), False
print s.isMatch("aa","aa"), True
print s.isMatch("aaa","aa"), False
print s.isMatch("aa", "*"), True
print s.isMatch("aa", "a*"), True
print s.isMatch("ab", "?*"), True
print s.isMatch("aab", "c*a*b"), False
