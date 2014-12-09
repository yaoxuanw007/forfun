# https://oj.leetcode.com/problems/search-in-rotated-sorted-array/

# Only work for the array in ascending order
class Solution:
  # @param A, a list of integers
  # @param target, an integer to be searched
  # @return an integer
  def search(self, A, target):
    left, right = 0, len(A) - 1
    while left <= right:
      mid = (left + right) / 2
      if A[mid] == target:
        return True
      elif A[mid] > A[right]:
        if target >= A[left] and target < A[mid]:
          right = mid - 1
        else:
          left = mid + 1
      elif A[mid] < A[right]:
        if target > A[mid] and target <= A[right]:
          left = mid + 1
        else:
          right = mid -1
      else:
        right -= 1
    return False

# Two orders and dup
class Solution1:
  # @param A, a list of integers
  # @param target, an integer to be searched
  # @return an integer
  def search(self, A, target):
    left, right = 0, len(A) - 1
    while left <= right:
      mid = (left + right) / 2
      if A[mid] == target:
        return True
      elif A[left] < A[right]:
        if A[mid] < A[left]:
          if A[mid] < target and target <= A[left]:
            right = mid - 1
          else:
            left = mid + 1
        elif A[mid] > A[right]:
          if A[right] <= target and target < A[mid]:
            left = mid + 1
          else:
            right = mid - 1
        elif A[left] < A[mid] and A[mid] < A[right]:
          if target < A[mid]:
            right = mid - 1
          else:
            left = mid + 1
        elif A[left] == A[mid]:
          left += 1
        else:
          right -= 1
      else:
        if A[mid] < A[right]:
          if A[mid] < target and target <= A[right]:
            left = mid + 1
          else:
            right = mid - 1
        elif A[mid] > A[left]:
          if A[left] <= target and target < A[mid]:
            right = mid - 1
          else:
            left = mid + 1
        elif A[right] < A[mid] and A[mid] < A[left]:
          if target < A[mid]:
            left = mid + 1
          else:
            right = mid - 1
        elif A[left] == A[mid]:
          left += 1
        else:
          right -= 1
    return False

s = Solution1()

print s.search([4,5,6,7,0,1,2], 2)
print s.search([2,1,0,7,6,5,4], 4)
print s.search([4,5,6,7,0,1,2], 0)
print s.search([0,1,2,4,5,6,7], 6)
print s.search([0,1,1,1,2,6,7], 6)
print s.search([0,1,1,1,2,6,7], 1)
