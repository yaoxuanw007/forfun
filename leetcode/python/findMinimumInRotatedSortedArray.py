# Question
# Find min in array: 4 5 6 7 0 1 2
# What if there are duplicates in array?
#
# Link: https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
#

# Assume that a < b < c
#
# [1, 2, 3, 4, 5] => a,b,c => L < R, L < M < R  => R = M
# [5, 4, 3, 2, 1] => c,b,a => L > R, L > M > R  => L = M
# [5, 1, 2, 3, 4] => c,a,b => L > R, L > M < R  => R = M
# [4, 3, 2, 1, 5] => b,a,c => L < R, L > M < R  => L = M
# [2, 3, 4, 5, 1] => b,c,a => L > R, L < M > R  => L = M
# [1, 5, 4, 3, 2] => a,c,b => L < R, L < M > R  => R = M

# [1, 2, 2, 2, 2] => a,b,b => L < R, L < M = R  => R = M
# [2, 2, 2, 2, 1] => b,b,a => L > R, L = M > R  => L = M

# [3, 2, 1, 0, 3] => b,a,b => L = R, L > M < R  => X
# [3, 0, 1, 2, 3] => b,a,b => L = R, L > M < R  => X

# [1, 1, 1, 0, 2] => a,a,b => L < R, L = M < R  => L = M
# [1, 1, 1, 2, 2] => a,a,b => L < R, L = M < R  => L = M
# [2, 0, 1, 1, 1] => b,a,a => L > R, L > M = R  => R = M
# [2, 2, 1, 1, 1] => b,a,a => L > R, L > M = R  => R = M

# [1, 0, 3, 2, 1] => a,b,a => L = R, L < M > R  => X
# [1, 2, 3, 0, 1] => a,b,a => L = R, L < M > R  => X

# [1, 2, 1, 1, 1] => a,a,a => L = R, L = M = R  => X
# [1, 1, 1, 2, 1]
# [1, 1, 1, 1, 1]

# [2, 1, 2, 2, 2] => b,b,b => L = R, L = M = R  => X
# [2, 2, 2, 1, 2]
# [2, 2, 2, 2, 2]

# special case
# [1, 2] => L < R, L = M < R                    => return L
# [1, 1] => L = R, L = M = R                    => return L
# [2, 1] => L > R, L = M > R                    => return R

# [1] => a => L = R, L = M = R                  => return L

#(L,R) - < - (L,M,R) - <,< - R = M
#                    - >,< - L = M
#                    - <,> - R = M
#                    - <,= - R = M
#                    - =,< - L = M
#      - > - (L,M,R) - >,> - L = M
#                    - >,< - R = M
#                    - <,> - L = M
#                    - =,> - L = M
#                    - >,= - R = M
#      - = - (L,M,R) - >,< - X
#                    - >,< - X
#                    - <,> - X
#                    - <,> - X
#                    - =,= - X
#                    - =,= - X
#
# Greedy Algorithm

# O(n)
class Solution2:
  def findMin(self, num):
    if len(num) > 0:
      mid, left, right = 0, 0, len(num) - 1
      while right - left > 1:
        mid = left + (right - left) / 2
        if num[left] == num[right]:
          left += 1
        elif num[left] < num[right]:
          # if M > min(L,R), closer to min(L,R)
          if num[left] < num[mid]:
            right = mid
          # closer to max(L,R)
          elif num[left] >= num[mid]:
            left = mid
        elif num[left] > num[right]:
          # if M > min(L,R), closer to min(L,R)
          if num[mid] > num[right]:
            left = mid
          # closer to max(L,R)
          elif num[mid] <= num[right]:
            right = mid
      mid = left if num[left] < num[right] else right
      return num[mid]
    else:
      return "no element!"

# O(logn) -> no dup
class Solution1:
  def findMin(self, num):
    if len(num) > 0:
      mid, left, right = 0, 0, len(num) - 1
      while right - left > 1:
        mid = left + (right - left) / 2
        # case 1:
        if num[left] < num[right]:
          if num[mid] > num[left]:
            right = mid
          elif num[mid] < num[left]:
            left = mid
        # case 2:
        elif num[left] > num[right]:
          if num[mid] > num[right]:
            left = mid
          elif num[mid] < num[right]:
            right = mid
      mid = left if num[left] < num[right] else right
      return num[mid]
    else:
      return "no element!"

noDupNums = [
    [1,3,5],
    [],
    [4, 5, 6, 7, 0, 1, 2],
    [4, 5, 6, 0, 1, 2, 3],
    [4],
    [4, 5],
    [4, 5, 3]
    ]

dupNums = [
    [0, 0, 0],
    [0, 0],
    [0],
    [1, 1, 0, 2],
    [1, 0, 2, 2],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [2, 2, 2, 2, 2, 0, 2],
    [2, 0, 2, 2, 2, 2, 2],
    [2, 2, 2, 0, 2, 2, 2],
    [1, 1, 0, 1, 1],
    [4, 4, 3, 2, 1, 0, 0, 5, 5, 5]
    ]

#######################################

s1 = Solution1()

print "no dup num"
for num in noDupNums:
  print s1.findMin(num)

#######################################

s2 = Solution2()

print "no dup num"
for num in noDupNums:
  print s2.findMin(num)

print "dup num"
for num in dupNums:
  print s2.findMin(num)
