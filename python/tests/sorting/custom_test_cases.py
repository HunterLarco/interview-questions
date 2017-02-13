import random
import unittest

class SortingTestCase(unittest.TestCase):
  @staticmethod
  def create_sorted_list(size):
    return range(size)

  @staticmethod
  def create_reversed_list(size):
    return range(size - 1, -1, -1)

  @staticmethod
  def create_shuffled_list(size):
    shuffled_list = range(size)
    random.shuffle(shuffled_list)
    return shuffled_list

  @staticmethod
  def create_duplicated_list(size, duplication=2):
    return range(size) * duplication

  @staticmethod
  def create_nearly_sorted_list(size, entropy=0.25):
    nearly_sorted_list = range(size)
    if size > 1:
      for _ in range(int(size * entropy)):
        i = random.randint(0, size - 2)
        nearly_sorted_list[i], nearly_sorted_list[i + 1] = nearly_sorted_list[i + 1], nearly_sorted_list[i]
    return nearly_sorted_list
