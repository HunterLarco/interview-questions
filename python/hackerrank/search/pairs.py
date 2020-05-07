# https://www.hackerrank.com/challenges/pairs/problem

from collections import Counter

def pairs(k, arr):
  targets = Counter()
  for value in arr:
    targets.update([value - k])

  count = 0
  for value in arr:
    count += targets[value]
  return count

def main():
  print(pairs(2, [1, 5, 3, 4, 2]))

if __name__ == '__main__':
  main()

