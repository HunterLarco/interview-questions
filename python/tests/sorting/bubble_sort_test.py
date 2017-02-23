import unittest

from python.sorting import bubble
from python.tests.sorting import custom_test_cases

class BubbleSortTest(custom_test_cases.SortingTestCase):
  def test_emptyList(self):
    self.assertEqual(bubble.bubble_sorted([]), [])

  def test_listWithOneElement(self):
    self.assertEqual(bubble.bubble_sorted([1]), [1])

  def test_reversedList(self):
    reversed_list = self.create_reversed_list(100)
    self.assertEqual(bubble.bubble_sorted(reversed_list), sorted(reversed_list))

  def test_sortedList(self):
    sorted_list = self.create_sorted_list(100)
    self.assertEqual(bubble.bubble_sorted(sorted_list), sorted(sorted_list))

  def test_duplicatedList(self):
    duplicated_list = self.create_duplicated_list(100)
    self.assertEqual(bubble.bubble_sorted(duplicated_list), sorted(duplicated_list))

  def test_shuffledList(self):
    shuffled_list = self.create_shuffled_list(100)
    self.assertEqual(bubble.bubble_sorted(shuffled_list), sorted(shuffled_list))

if __name__ == '__main__':
  unittest.main()
