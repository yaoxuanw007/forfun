# https://oj.leetcode.com/problems/rotate-image/

class Solution:
  # @param matrix, a list of lists of integers
  # @return a list of lists of integers
  def rotate(self, matrix):
    mLen = len(matrix)
    for i in xrange(mLen / 2):
      rLen = mLen - 1
      for j in xrange(i, rLen-i):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[rLen-j][i]
        matrix[rLen-j][i] = matrix[rLen-i][rLen-j]
        matrix[rLen-i][rLen-j] = matrix[j][rLen-i]
        matrix[j][rLen-i] = tmp
    return matrix

s = Solution()

print s.rotate([[1]])
print s.rotate([[1,2],[3,4]])
print s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
