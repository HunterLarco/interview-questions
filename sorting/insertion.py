def insertion_inplace(arr):
  for i, value in enumerate(arr):
    for j in range(i - 1, -1, -1):
      if arr[j] > value:
        arr[j + 1] = arr[j]
      else:
        arr[j + 1] = value
        break
    else:
      arr[0] = value

def insertion(arr):
  arr_copy = arr[:]
  insertion_inplace(arr_copy)
  return arr_copy

def main():
  assert insertion([]) == []
  assert insertion([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert insertion([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert insertion([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert insertion([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()
