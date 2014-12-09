# https://oj.leetcode.com/problems/single-number-ii/

class Solution:
  # @param A, a list of integer
  # @return an integer
  def singleNumber(self, A):
    # states[j]:
    #   If the bit is states[j] is 1, we have seen 1 for (k*3+(j+1)) times.
    #   At any time, each bit can only have at most one 1 in states array.
    # finite state machine: if we encounter 1, state 1 -> state 2 -> state 3 -> state 1 again
    states = [0, 0, 0]
    for e in A:
      for j in xrange(len(states)):
        # move to next state if bit is in current state and bit in element is 1
        states[(j+1)%3] |= states[j] & e
        # update state and element
        states[j], e = states[j] & (states[j] ^ e), e & (states[j] ^ e)
      # If we haven't seen any 1, move to state 1
      states[0] ^= e
    # number in state 1 is the single number
    return states[0]

s = Solution()

print s.singleNumber([3,3,2,3,2,18,2])
print s.singleNumber([0,1,0,1,0,1,2])


# Given A = [0, 1, 0, 1, 0, 1, x] and states = [0, 0, 0]
#
# e = A[i]
#
# nextIndex = (j+1)%3
#
# Take 1 bit as an example:
#
# if states[j] == 0 and e == 0, states[j] = 0, states[nextIndex] |= 0, e = 0
# => haven't seen any 1 and element is 0, don't change states
# if states[j] == 0 and e == 1, states[j] = 0, states[nextIndex] |= 0, e = 1
# => haven't seen any 1 and element is 1, don't change states and keep process this element
# if states[j] == 1 and e == 0, states[j] = 1, states[nextIndex] |= 0, e = 0
# => see 1 and element is 0, don't change states
# if states[j] == 1 and e == 1, states[j] = 0, states[nextIndex] |= 1, e = 0
# => see 1 and element is 1, move to next state and reset element because we have used this
