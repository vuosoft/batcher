
import unittest
import sys
sys.path.append("../")
from batcherlib.main import addnumbers
from batcherlib.main import batcher



class TestBatcher(unittest.TestCase):

    def setUp(self):
        self.records1 = ["1234", "123456", "12", "12345678901"] 


    def test_batcher1(self):
        response = batcher(self.records1)
        self.assertEqual(len(response), 3, "Should be 3")

    def test_batcher2(self):
        response = batcher(self.records1)
        self.assertEqual(len(response[0]), 2, "Should be 2")

    def test_batcher3(self):
        response = batcher(self.records1)
        self.assertEqual(len(response[1]), 1, "Should be 1")

    def test_batcher4(self):
        response = batcher(self.records1)
        self.assertEqual(len(response[2]), 1, "Should be 1")

    def test_sanity(self):
        self.assertEqual(addnumbers(4, 2), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()