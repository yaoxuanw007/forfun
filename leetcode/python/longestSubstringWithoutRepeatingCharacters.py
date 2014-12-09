# https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
  # @return an integer
  def lengthOfLongestSubstring(self, s):
    currLen, maxLen, start, hasFound = 0, 0, 0, {}
    for i in xrange(len(s)):
      if s[i] in hasFound and hasFound[s[i]] >= 1:
        hasFound[s[i]] += 1
        currLen += 1
        while True:
          hasFound[s[start]] -= 1
          currLen -= 1
          start += 1
          if s[start-1] == s[i]:
            break
      else:
        hasFound[s[i]] = 1
        currLen += 1
      if currLen > maxLen:
        maxLen = currLen
    return maxLen

s = Solution()

print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac")
