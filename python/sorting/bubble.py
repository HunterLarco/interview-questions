# -*- coding: utf-8 -*-
"""Bubble Sort implementation."""

def bubble_sort(arr):
  """Executes a bubble sort in-place.

  To learn about bubble sort, visit https://en.wikipedia.org/wiki/Bubble_sort

  Args:
      arr (list of any comparable type): The list that will be sorted via
          bubble sort.
  """
  while True:
    preformed_swap = False
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        preformed_swap = True
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if not preformed_swap:
      break

def bubble_sorted(arr):
  """Executes a bubble sort out of place akin to python's "sorted" builtin.

  To learn about bubble sort, visit https://en.wikipedia.org/wiki/Bubble_sort

  Args:
      arr (list of any comparable type): The list that will be sorted via
          bubble sort.

  Returns:
      list of objects: A sorted copy of the parameter `arr`.
  """
  arr_copy = arr[:]
  bubble_sort(arr_copy)
  return arr_copy
