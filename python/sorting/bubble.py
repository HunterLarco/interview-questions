# -*- coding: utf-8 -*-
"""Bubble Sort implementation."""

def bubble_sort(arr, section=slice(None)):
  """Executes a bubble sort in-place.

  To learn about bubble sort, visit https://en.wikipedia.org/wiki/Bubble_sort

  Args:
      arr (list of any comparable type): The list that will be sorted via
          bubble sort.
      section (:obj:`slice`, optional): Determines the section of the provided
          list that will be sorted. Defaults to the entire array.
  """
  step = section.step if not section.step is None else 1
  while True:
    preformed_swap = False
    for i in range(*section.indices(len(arr) - step)):
      if arr[i] > arr[i + step]:
        preformed_swap = True
        arr[i], arr[i + step] = arr[i + step], arr[i]
    if not preformed_swap:
      break

def bubble_sorted(arr, section=slice(None)):
  """Executes a bubble sort out of place akin to python's "sorted" builtin.

  To learn about bubble sort, visit https://en.wikipedia.org/wiki/Bubble_sort

  Args:
      arr (list of any comparable type): The list that will be sorted via
          bubble sort.
      section (:obj:`slice`, optional): Determines the section of the provided
          list that will be sorted. Defaults to the entire array.

  Returns:
      list of objects: A sorted copy of the parameter ``arr``.
  """
  arr_copy = arr[section]
  bubble_sort(arr_copy)
  return arr_copy
