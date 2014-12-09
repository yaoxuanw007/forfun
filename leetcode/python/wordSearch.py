# https://oj.leetcode.com/problems/word-search/

class Solution:
  # @param board, a list of lists of 1 length string
  # @param word, a string
  # @return a boolean
  def exist(self, board, word):
    if len(word) == 0:
      return False

    self.rLen, self.cLen, self.wLen = len(board), len(board[0]), len(word)
    self.used = [[False]*self.cLen for i in xrange(self.rLen)]
    for i in xrange(self.rLen):
      for j in xrange(self.cLen):
        if self.walk(board, word, (i,j), 0):
          return True
    return False

  # n is the index of word
  def walk(self, board, word, pos, n):
    if pos[0] < 0 or pos[0] >= self.rLen or pos[1] < 0 or pos[1] >= self.cLen:
      return False
    if self.used[pos[0]][pos[1]] or board[pos[0]][pos[1]] != word[n]:
      return False
    if n == self.wLen - 1:
      return True
    elif n < self.wLen - 1:
      self.used[pos[0]][pos[1]] = True
      for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newPos = (pos[0]+d[0], pos[1]+d[1])
        if self.walk(board, word, newPos, n+1):
          return True
      self.used[pos[0]][pos[1]] = False
    return False

s = Solution()

board = ["ABCE","SFCS","ADEE"]
print s.exist(board, "ABCCED")
print s.exist(board, "SEE")
print s.exist(board, "ABCB")

print s.exist(["aa"], "aa")
