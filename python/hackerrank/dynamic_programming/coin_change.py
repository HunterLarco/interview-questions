# https://www.hackerrank.com/challenges/ctci-coin-change/problem

def ways(n, coins):
  history = [1] + [0] * n

  for coin in coins:
    for i in range(1, n + 1):
      if i - coin >= 0:
        history[i] += history[i - coin]

  return history[-1]

def main():
  print(ways(12, [1, 2, 5, 10]))

if __name__ == '__main__':
  main()

