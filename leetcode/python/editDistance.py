# https://oj.leetcode.com/problems/edit-distance/

# DP Time: O(n*m); Space: O(n*m)
class Solution:
  # @return an integer
  def minDistance(self, word1, word2):
    n, m = len(word1), len(word2)
    # Don't create array using [[0] * (m+1)] * (n+1)
    table = [[0] * (m+1) for i in xrange(0, n+1)]

    for i in xrange(1, n + 1):
      table[i][0] = table[i-1][0] + 1

    for j in xrange(1, m + 1):
      table[0][j] = table[0][j-1] + 1

    for i in xrange(1, n + 1):
      for j in xrange(1, m + 1):
        replace = 1
        # replace the last charactor of word1 and word2 are different
        if word1[i-1] == word2[j-1]:
          replace = 0
        # get the minimum of insert, delete, replace or do nothing
        table[i][j] = min(table[i][j-1] + 1, table[i-1][j] + 1, table[i-1][j-1] + replace)

    return table[n][m]

s = Solution()
print s.minDistance("a", "ab")
print s.minDistance("ac", "ab")
print s.minDistance("abd", "ab")
print s.minDistance("", "ab")
print s.minDistance("ab", "")
