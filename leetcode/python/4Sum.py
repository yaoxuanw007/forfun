# https://oj.leetcode.com/problems/4sum/

class Solution:
  # Time Limit Excess
  # O(n^3)
  # @return a list of lists of length 4, [[val1,val2,val3,val4]]
  # def fourSum(self, num, target):
  #   num = sorted(num)
  #   result, i = [], 0
  #   # first number
  #   while i < len(num) - 3:
  #     j = i + 1
  #     # second number
  #     while j < len(num) - 2:
  #       newTarget = target - num[i] - num[j]
  #       m, n = j+1, len(num)-1
  #       # 3nd and 4th numbers
  #       while m < n:
  #         value = num[m] + num[n]
  #         if value == newTarget:
  #           result.append([num[i], num[j], num[m], num[n]])
  #         if value <= newTarget:
  #           # skip same value
  #           while m < n and num[m] == num[m+1]:
  #             m += 1
  #           m += 1
  #         if value >= newTarget:
  #           # skip same value
  #           while n > m and num[n] == num[n-1]:
  #             n -= 1
  #           n -= 1
  #       # skip same value
  #       while j < len(num) - 2 and num[j] == num[j+1]:
  #         j += 1
  #       j += 1
  #     # skip same value
  #     while i < len(num) - 3 and num[i] == num[i+1]:
  #       i += 1
  #     i += 1
  #   return result

  # Accepted!
  def fourSum(self, num, target):
    num = sorted(num)
    result, twoSumDict = set(), {}
    # get all sum of two numbers
    for i in xrange(len(num)-1):
      for j in xrange(i+1, len(num)):
        twoSum = num[i] + num[j]
        if twoSum not in twoSumDict:
          twoSumDict[twoSum] = []
        # add index
        twoSumDict[twoSum].append(set([i, j]))
    # make sure there is no duplicate process
    hasFound = []
    for twoSum in twoSumDict.keys():
      if twoSum in hasFound:
        continue
      otherTwoSum = target - twoSum
      if otherTwoSum in twoSumDict:
        hasFound.append(otherTwoSum)
        comb1 = twoSumDict[twoSum]
        if twoSum == otherTwoSum:
          for i in xrange(len(comb1)-1):
            for j in xrange(i+1, len(comb1)):
              unionComb = comb1[i] | comb1[j]
              # Make sure we use each number at most once
              if len(unionComb) == 4:
                # Make sure the result is in non-descending order
                result.add(tuple([num[x] for x in sorted(unionComb)]))
        else:
          comb2 = twoSumDict[otherTwoSum]
          for i in xrange(len(comb1)):
            for j in xrange(len(comb2)):
              unionComb = comb1[i] | comb2[j]
              # Make sure we use each number at most once
              if len(unionComb) == 4:
                result.add(tuple([num[x] for x in sorted(unionComb)]))
    return [list(x) for x in result]

s = Solution()

print s.fourSum([1,0,-1,0,-2,2], 0)
