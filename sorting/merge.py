# TODO(hunterlarco) Preform this in-place.
def merge(arr):
  if len(arr) < 2: return arr

  # Divide
  middle = len(arr) // 2
  left = merge(arr[:middle])
  right = merge(arr[middle:])

  # Combine
  combined = []
  while left and right:
    if left[0] <= right[0]:
      combined.append(left.pop(0))
    else:
      combined.append(right.pop(0))
  combined += left + right

  return combined

def main():
  assert merge([]) == []
  assert merge([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert merge([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
  assert merge([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
  assert merge([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
  print "PASSED"

if __name__ == '__main__':
  main()