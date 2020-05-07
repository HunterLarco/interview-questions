# https://www.hackerrank.com/challenges/count-triplets-1/problem

from collections import Counter

def countTriplets(arr, r):
  ahead_count = Counter(arr)
  behind_count = Counter()

  count = 0
  for value in arr:
    ahead_count.subtract([value])
    count += behind_count[value / r] * ahead_count[value * r]
    behind_count.update([value])
  return count

def main():
  print(countTriplets([1] * 100000, 1))

if __name__ == '__main__':
  main()
