def selection_inplace(arr):
  for i in range(len(arr) - 1):
    pocket_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[pocket_index]:
        pocket_index = j
    if pocket_index != i:
      arr[i], arr[pocket_index] = arr[pocket_index], arr[i]

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
