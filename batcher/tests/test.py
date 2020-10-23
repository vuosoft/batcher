
import unittest
import sys
sys.path.append("../")
from batcherlib.utils import addnumbers



class TestBatcher(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_add(self):
        self.assertEqual(addnumbers(4, 2), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()