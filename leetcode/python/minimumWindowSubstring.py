# https://oj.leetcode.com/problems/minimum-window-substring/

class Solution:
  # @return a string
  def minWindow(self, S, T):
    needToFind, hasFound = {}, {}
    sLen, tLen = len(S), len(T)

    for c in T:
      if c not in needToFind:
        needToFind[c] = 1
        hasFound[c] = 0
      else:
        needToFind[c] += 1

    minLen = sLen + 1
    # minEnd set to -1, then return "" if we found nothing
    minStart, minEnd = 0, -1
    start, count = 0, 0
    for end in xrange(0, sLen):
      if S[end] not in needToFind:
        continue

      hasFound[S[end]] += 1
      if hasFound[S[end]] <= needToFind[S[end]]:
        count += 1

      if count == tLen:
        while True:
          if S[start] in needToFind:
            if hasFound[S[start]] <= needToFind[S[start]]:
              break
            hasFound[S[start]] -= 1
          start += 1

        currLen = end - start + 1
        if minLen > currLen:
          minLen = currLen
          minStart = start
          minEnd = end

    return S[minStart:minEnd+1]

s = Solution()

print s.minWindow("ADOBECODEBANC", "ABC")
print s.minWindow("a", "a")
print s.minWindow("a", "aa")



