# https://oj.leetcode.com/problems/longest-common-prefix/

class Solution:
  # @return a string
  def longestCommonPrefix(self, strs):
    prefix = ""
    if len(strs) > 0:
      prefix = strs[0]
      for i in xrange(1, len(strs)):
        # set the short one as prefix
        curr = strs[i]
        if len(strs[i]) < len(prefix):
          curr = prefix
          prefix = strs[i]
        # find the common prefix
        for j in xrange(0, len(prefix)):
          if prefix[j] != curr[j]:
            prefix = prefix[:j]
            break
    return prefix

s = Solution()

print s.longestCommonPrefix(["ab", "a"]), "a"
print s.longestCommonPrefix(["c", "ab"]), ""
print s.longestCommonPrefix(["a", "ab"]), "a"
print s.longestCommonPrefix(["", "ab"]), ""
print s.longestCommonPrefix(["ab", ""]), ""
print s.longestCommonPrefix([]), ""
