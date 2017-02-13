import random
import unittest

from sorting import bubble
 
class BubbleSortTest(unittest.TestCase):
  def test_emptyList(self):
    self.assertEqual(bubble.bubble([]), [])

  def test_listWithOneElement(self):
    self.assertEqual(bubble.bubble([1]), [1])

  def test_reversedList(self):
    self.assertEqual(bubble.bubble(list(range(100, 0, -1))), sorted(range(100, 0, -1)))

  def test_sortedList(self):
    self.assertEqual(bubble.bubble(list(range(0, 100))), list(range(0, 100)))

  def test_duplicatedList(self):
    duplicated_list = list(range(100, 0, -1)) + list(range(100, 0, -1))
    self.assertEqual(bubble.bubble(duplicated_list), sorted(duplicated_list))

  def test_shuffledList(self):
    shuffled = range(100)
    random.shuffle(shuffled)
    self.assertEqual(bubble.bubble(shuffled), sorted(shuffled))

if __name__ == '__main__':
  unittest.main()
