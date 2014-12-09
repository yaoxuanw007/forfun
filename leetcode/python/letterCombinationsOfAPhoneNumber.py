# https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
  # @return a list of strings, [s1, s2]
  def letterCombinations(self, digits):
    result = ['']
    letters = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    for i in xrange(len(digits)):
      nextResult, digit = [], int(digits[i])
      for j in xrange(len(result)):
        if digit > 1 and digit <= 9:
          for letter in letters[digit-2]:
            nextResult.append(result[j] + letter)
        else:
          # add the original strings
          nextResult.append(result[j])
      # get new result
      result = nextResult
    return result

s = Solution()

print s.letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


