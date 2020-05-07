# https://www.hackerrank.com/challenges/special-palindrome-again/problem

class Sequence(object):
  def __init__(self, letter, count=1):
    self.letter = letter
    self.count = count

  def __repr__(self):
    return 'Sequence(%s, %d)' % (self.letter, self.count)

def substrCount(s):
  rope = []
  for value in s:
    if rope and value == rope[-1].letter:
      rope[-1].count += 1
    else:
      rope.append(Sequence(value))

  count = 0

  for sequence in rope:
    count += sequence.count * (sequence.count + 1) // 2

  for i in range(2, len(rope)):
    before = rope[i - 2]
    middle = rope[i - 1]
    after = rope[i]

    if middle.count == 1 and before.letter == after.letter:
      count += min(before.count, after.count)

  return count

def main():
  print(substrCount('mnonopoo'))

if __name__ == '__main__':
  main()

