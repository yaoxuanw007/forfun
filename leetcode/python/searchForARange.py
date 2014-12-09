# https://oj.leetcode.com/problems/search-for-a-range/

class Solution:
  # @param A, a list of integers
  # @param target, an integer to be searched
  # @return a list of length 2, [index1, index2]
  def searchRange(self, A, target):
    result = [-1, -1]
    if len(A) == 0 or target < A[0] or target > A[-1]:
      return result
    left, right, found = 0, len(A) - 1, -1
    while left <= right:
      mid = (left + right) / 2
      if target == A[mid]:
        found = mid
        break
      elif target < A[mid]:
        right = mid - 1
      else:
        left = mid + 1

    if found >= 0:
      result[0] = self.searchBoundary(A, 0, found, target, True)
      result[1] = self.searchBoundary(A, found, len(A) - 1, target, False)

    return result

  def searchBoundary(self, A, left, right, target, isStart):
    # At last, right == left - 1
    while left <= right:
      mid = (left + right) / 2
      if isStart:
        # At last, left = target
        if target == A[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        # At last, right = target
        if target == A[mid]:
          left = mid + 1
        else:
          right = mid - 1
    return left if isStart else right

s = Solution()

print s.searchRange([1], 1)
print s.searchRange([2, 2], 2)
print s.searchRange([1,3,4], 2)
print s.searchRange([5, 7, 7, 8, 8, 10], 8)
