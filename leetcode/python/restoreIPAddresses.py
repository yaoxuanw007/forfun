# https://oj.leetcode.com/problems/restore-ip-addresses/

class Solution:
  # @param s, a string
  # @return a list of strings
  def restoreIpAddresses(self, s):
    self.result = []
    self.restoreIp(s, 4, [])
    return self.result

  def restoreIp(self, s, n, path):
    if n == 0:
      if s == "":
        self.result.append('.'.join(path))
      return
    for i in xrange(3):
      num = s[:i+1]
      if not self.isValidPart(num) or i >= len(s):
        break
      path.append(num)
      self.restoreIp(s[i+1:], n - 1, path)
      path.pop()

  def isValidPart(self, s):
    if s == "":
      return False
    if len(s) >= 2 and s[0] == '0':
      return False
    num = int(s)
    if num >= 0 and num <= 255:
      return True
    return False

s = Solution()

print s.restoreIpAddresses("25525511135")
