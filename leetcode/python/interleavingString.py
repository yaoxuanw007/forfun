# https://oj.leetcode.com/problems/interleaving-string/

# DP Time O(n*m); Space O(n*m)
class Solution:
  # @return a boolean
  def isInterleave(self, s1, s2, s3):
    n, m = len(s1), len(s2)
    if n + m != len(s3):
      return False

    # don't use [[False] * (m+1)] * (n+1)
    table = [[False] * (m+1) for i in xrange(0, n+1)]

    # because n + m == len(s3), so two variables is enough
    # table[i][j]: interleave with s1[:i] and s2[:j]

    # base cases
    table[0][0] = True
    for i in xrange(1, n+1):
      table[i][0] = table[i-1][0] and s1[i-1] == s3[i-1]
    for j in xrange(1, m+1):
      table[0][j] = table[0][j-1] and s2[j-1] == s3[j-1]

    for i in xrange(1, n+1):
      for j in xrange(1, m+1):
        table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])

    return table[n][m]

s = Solution()

print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
print s.isInterleave("aabc", "abad", "aabadabc")
print s.isInterleave("ab", "bc", "babc")

