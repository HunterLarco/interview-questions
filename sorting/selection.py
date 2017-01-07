def selection_inplace(arr):
  for i in range(len(arr) - 1):
    pocket_index, pocket = min(enumerate(arr[i] for i in range(i, len(arr))), key=lambda x: (x[1], x[0]))
    arr[i], arr[pocket_index + i] = arr[pocket_index + i], arr[i]

def selection(arr):
  arr_copy = arr[:]
  selection_inplace(arr_copy)
  return arr_copy

def main():
  assert selection([]) == []
  assert selection([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert selection([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert selection([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert selection([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()
