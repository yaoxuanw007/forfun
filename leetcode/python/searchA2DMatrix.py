# https://oj.leetcode.com/problems/search-a-2d-matrix/

class Solution:
  # @param matrix, a list of lists of integers
  # @param target, an integer
  # @return a boolean
  def searchMatrix(self, matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m - 1
    while left <= right:
      mid = (left + right) / 2
      if matrix[mid][0] == target:
        return True
      elif matrix[mid][0] < target:
        left = mid + 1
      else:
        right = mid - 1

    leftMid = mid
    if matrix[mid][0] > target:
      leftMid = mid - 1

    if matrix[leftMid][n-1] < target:
      return False

    left, right = 0, n - 1
    while left <= right:
      mid = (left + right) / 2
      if matrix[leftMid][mid] == target:
        return True
      elif matrix[leftMid][mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return False

s = Solution()

print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 8)
print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 2)
print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11)
