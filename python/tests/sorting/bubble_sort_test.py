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

  def test_emptyList_withSection(self):
    self.assertEqual(bubble.bubble_sorted([], section=slice(3, 5)), [])

  def test_listWithOneElement_withSection_included(self):
    self.assertEqual(bubble.bubble_sorted([1], section=slice(0, 5)), [1])

  def test_listWithOneElement_withSection_excluded(self):
    self.assertEqual(bubble.bubble_sorted([1], section=slice(3, 5)), [])

  def test_reversedList_withSection_outOfPlace(self):
    reversed_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    self.assertEqual(
        bubble.bubble_sorted(reversed_list, section=slice(2, -2)),
        [2, 3, 4, 5, 6, 7])
    self.assertEqual(
        bubble.bubble_sorted(reversed_list, section=slice(-2)),
        [2, 3, 4, 5, 6, 7, 8, 9])
    self.assertEqual(
        bubble.bubble_sorted(reversed_list, section=slice(None, -2, 2)),
        [3, 5, 7, 9])

  def test_reversedList_withSection_inPlace(self):
    reversed_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    bubble.bubble_sort(reversed_list, section=slice(2, -2))
    self.assertEqual(reversed_list, [9, 8, 2, 3, 4, 5, 6, 7, 1, 0])

    reversed_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    bubble.bubble_sort(reversed_list, section=slice(-2))
    self.assertEqual(reversed_list, [2, 3, 4, 5, 6, 7, 8, 9, 1, 0])

    reversed_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    bubble.bubble_sort(reversed_list, section=slice(None, -2, 2))
    self.assertEqual(reversed_list, [3, 8, 5, 6, 7, 4, 9, 2, 1, 0])

if __name__ == '__main__':
  unittest.main()
