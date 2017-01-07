def gnome_inplace(arr):
  for i, value in enumerate(arr):
    for j in range(i - 1, -1, -1):
      if arr[j] > value:
        arr[j + 1], arr[j] = arr[j], arr[j + 1]
      else:
        break

def gnome(arr):
  arr_copy = arr[:]
  gnome_inplace(arr_copy)
  return arr_copy

def main():
  assert gnome([]) == []
  assert gnome([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert gnome([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert gnome([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert gnome([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()
