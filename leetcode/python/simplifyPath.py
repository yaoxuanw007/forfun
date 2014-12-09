# https://oj.leetcode.com/problems/simplify-path/

class Solution:
  # @param path, a string
  # @return a string
  def simplifyPath(self, path):
    result, curr = [], ""
    for i in xrange(len(path)):
      # get current part between /
      if path[i] != '/':
        curr += path[i]
      # If it's / or last charactor
      if path[i] == '/' or i == len(path) - 1:
        # duplicate /
        if len(curr) == 0:
          continue
        # previous directory
        if curr == '..':
          if len(result) > 0:
            result.pop(-1)
        # skip current directory
        elif curr != '.':
          result.append(curr)
        # clean current part
        curr = ""
    simplePath = ['/'+x for x in result]
    if len(simplePath) == 0:
      return '/'
    return ''.join(simplePath)

