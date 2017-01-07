# TODO(hunterlarco) Preform this in-place.
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
  assert quick([]) == []
  assert quick([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert quick([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert quick([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert quick([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()