# https://oj.leetcode.com/problems/text-justification/

class Solution:
  # @param words, a list of strings
  # @param L, an integer
  # @return a list of strings
  def fullJustify(self, words, L):
    count, line, lines = 0, [], []
    for word in words:
      count += len(word)
      if count > L:
        count -= len(word)
        lines.append(self.createLine(L, line, count, False))
        # prepare for next line
        line = [word]
        count = len(word) + 1
      else:
        line.append(word)
        count += 1
    # special case: words is empty
    if len(words) > 0:
      lines.append(self.createLine(L, line, count, True))

    # print [len(x) for x in lines]

    return lines

  # generate each line
  def createLine(self, L, line, count, isLastLine):
    # add every one space back
    extraLen = L - count + len(line)
    slotCount = len(line) - 1

    # special case: one word per line
    if slotCount == 0:
      slotLen = 0
      extraCount = 0
    # special case: last line (multiple words)
    elif isLastLine:
      slotLen = 1
      extraCount = 0
      extraLen -= len(line)
    else:
      slotLen = extraLen / slotCount
      extraCount = extraLen % slotCount
      extraLen = 0

    # process current line
    currLine = ""
    for currWord in line:
      currLine += currWord
      currLine += (" " * slotLen)
      if extraCount > 0:
        currLine += " "
        extraCount -= 1
    currLine += (" " * extraLen)

    # special case: one word in non-last line
    if slotCount > 0 and not isLastLine:
      # remove last slotLen
      return currLine[:-1*slotLen]
    else:
      return currLine

s = Solution()

print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print s.fullJustify([], 16)
print s.fullJustify(["What","must","be","shall","be."], 12)
