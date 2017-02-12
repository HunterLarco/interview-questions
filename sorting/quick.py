def quick_inplace(arr, start=0, end=-1):
  if len(arr) < 2: return
  if end < 0: end += len(arr)
  if end < 0: raise IndexError('list index out of range')
  if end - start < 2: return
  pivot = arr[start]
  i = start + 1
  j = end
  while i < j:
    while i <= j and arr[i] < pivot:
      i += 1
    while i <= j and arr[j] > pivot:
      j -= 1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1
  arr[start], arr[j] = arr[j], arr[start]
  if i - 1 > 0: quick_inplace(arr, start=start, end=i - 1)
  quick_inplace(arr, start=j + 1, end=end)

def quick(arr):
  if len(arr) < 2: return arr

  pivot = arr[0]
  left = []
  right = []
  pivots = []

  for item in arr:
    if item < pivot:
      left.append(item)
    elif item == pivot:
      pivots.append(item)
    else:
      right.append(item)

  return quick(left) + pivots + quick(right)

def main():
  test([], [])
  test([1, 2, 3, 4, 5], range(1, 6))
  test([5, 4, 3, 2, 1], range(1, 6))
  test([5, 2, 3, 4, 1], range(1, 6))
  test([1, 5, 2, 4, 3], range(1, 6))
  print "PASSED"

def test(arr, expected):
  quick_inplace(arr)
  assert arr == expected

if __name__ == '__main__':
  main()