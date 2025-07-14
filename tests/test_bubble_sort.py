import unittest

from ..bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble(self):
        list = [24,46,11,8,67,12]
        expected_list = [8,12,11,24,46,67]

        list = bubble_sort(list)
        self.assertEqual(list, expected_list)

if __name__ == '__main__':
    unittest.main()