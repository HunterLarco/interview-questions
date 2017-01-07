def heap_inplace(arr):
  # Construct heap
  for i in range(len(arr)):
    fix_upward(arr, i)

  # Sort
  for i in range(len(arr) - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    fix_downward(arr, 0, i)

def fix_upward(arr, index):
  if index == 0: return
  root_index = parent(index)
  if arr[root_index] < arr[index]:
    arr[root_index], arr[index] = arr[index], arr[root_index]
    fix_upward(arr, root_index)

def parent(index):
  return (index - 1) // 2

def fix_downward(arr, index, size):
  left_index, right_index = children(index)
  if left_index < size and right_index < size:
    if arr[left_index] > arr[right_index] and arr[left_index] > arr[index]:
      arr[left_index], arr[index] = arr[index], arr[left_index]
      fix_downward(arr, left_index, size)
    elif arr[right_index] >= arr[left_index] and arr[right_index] > arr[index]:
      arr[right_index], arr[index] = arr[index], arr[right_index]
      fix_downward(arr, right_index, size)
  elif left_index < size and arr[left_index] > arr[index]:
    arr[left_index], arr[index] = arr[index], arr[left_index]
    fix_downward(arr, left_index, size)

def children(index):
  return index * 2 + 1, index * 2 + 2

def heap(arr):
  arr_copy = arr[:]
  heap_inplace(arr_copy)
  return arr_copy

def main():
  assert heap([]) == []
  assert heap([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert heap([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert heap([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert heap([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()
