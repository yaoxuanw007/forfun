# https://oj.leetcode.com/problems/candy/

# O(nlogn)
class Solution:
  # @param ratings, a list of integer
  # @return an integer
  def candy(self, ratings):
    size = len(ratings)
    if size == 0:
      return 0

    # O(nlogn)
    sortedChildren = sorted(
        [(ratings[i], i) for i in xrange(0, size)],key=lambda x: x[0])
    candies = [0] * size
    # O(n)
    for child in sortedChildren:
      candies[child[1]] = self.minCandy(child[1], ratings, candies)
    # print candies
    return sum(candies)

  def minCandy(self, pos, ratings, candies):
    minPos = 0
    maxPos = len(ratings)-1

    result = 1
    rating = ratings[pos]
    candy = candies[pos]
    if pos > minPos:
      otherRating = ratings[pos-1]
      otherCandy = candies[pos-1]
      if otherRating < rating:
        result = max(result, otherCandy+1)
    if pos < maxPos:
      otherRating = ratings[pos+1]
      otherCandy = candies[pos+1]
      if otherRating < rating:
        result = max(result, otherCandy+1)
    return result

s = Solution()

inputs = [
    [2, 1, 3]
    ]

for ratings in inputs:
  print s.candy(ratings)
