def bubble_inplace(arr):
  while True:
    preformed_swap = False
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        preformed_swap = True
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if not preformed_swap:
      return arr

def bubble(arr):
  arr_copy = arr[:]
  bubble_inplace(arr_copy)
  return arr_copy

def main():
  assert bubble([]) == []
  assert bubble([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert bubble([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert bubble([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert bubble([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()
