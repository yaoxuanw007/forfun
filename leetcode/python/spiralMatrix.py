# https://oj.leetcode.com/problems/spiral-matrix/

class Solution:
  # @param matrix, a list of lists of integers
  # @return a list of integers
  def spiralOrder(self, matrix):
    result = []
    if len(matrix) > 0 and len(matrix[0]) > 0:
      m, n = len(matrix), len(matrix[0])
      for k in xrange(min(n, m) / 2):
        for j in xrange(k, n-1-k):
          result.append(matrix[k][j])
        for i in xrange(k, m-1-k):
          result.append(matrix[i][n-1-k])
        for j in xrange(k, n-1-k):
          result.append(matrix[m-1-k][n-1-j])
        for i in xrange(k, m-1-k):
          result.append(matrix[m-1-i][k])
      k = min(n, m) / 2
      if min(n, m) % 2 == 1:
        if m > n:
          for i in xrange(k, m-k):
            result.append(matrix[i][k])
        else:
          for j in xrange(k, n-k):
            result.append(matrix[k][j])
    return result

s = Solution()

print s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]), [1,2,3,6,9,8,7,4,5]
print s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ]])
print s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ], [ 7, 8, 9 ], [ 10, 11, 12 ]])
print s.spiralOrder([[ 1, 2 ],[ 3, 4 ]])
print s.spiralOrder([[ 1 ]])
print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
