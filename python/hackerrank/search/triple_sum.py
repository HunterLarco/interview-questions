# https://www.hackerrank.com/challenges/triple-sum/problem

def triplets(a, b, c):
  a = sorted(set(a))
  b = sorted(set(b))
  c = sorted(set(c))

  before = 0
  after = 0

  count = 0
  for q in b:
    while before < len(a) and a[before] <= q:
      before += 1
    while after < len(c) and c[after] <= q:
      after += 1
    count += before * after
  return count

def main():
  print(triplets([3, 5, 7], [3, 6], [4, 6, 9]))

if __name__ == '__main__':
  main()

