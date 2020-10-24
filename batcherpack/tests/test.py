import unittest
import sys
import math
sys.path.append("../")
from batcherlib.main import batcher
from random import random
from random import choices
from math import trunc

TEST_SMALL_MAX_RECORD_SIZE = 9
TEST_SMALL_MAX_BATCH_SIZE = 50 
TEST_SMALL_MAX_RECORDS_IN_BATCH = 6

UNICODE_ELEMENTS = "aēbcŽdefghi" + u'\0041' + u'\0042' + " jklmnopqrstuvxyzåäö" + u'\0043' u'\0044'
ASCII_ELEMENTS = "abcdefghijklmnopqrstuvxyz"

def generate_random_size_record(unicode=True, multiplier=1):
    """
    Returns a random size string. 
    By defining unicode=True, returned string contains unicode characters.
    Multiprier is used to create an oversize record by giving 
    multiplier > 1.  
    """
    if unicode:
        elements = UNICODE_ELEMENTS
    else:
        elements = ASCII_ELEMENTS

    return ''.join(choices(elements, k=math.trunc((random() * MAX_RECORD_SIZE * multiplier) + 1)))


def generate_fixed_size_record(unicode=True,size=1):
    """
    Returns a fixed size string. 
    Unicode defines does the returned string contain unicode characters
    Size defines the size of returned string
    """
    if unicode:
        elements = UNICODE_ELEMENTS
    else:
        elements = ASCII_ELEMENTS
    return ''.join(choices(elements, k=size))


class TestBatcher(unittest.TestCase):

    def setUp(self):
        self.records1 = ["1234", "123456", "12", "12345678901", "123", "123456", "12", "12345678901", "1234", "123456"] 

    def test_splitting1(self):
        response = batcher(self.records1, TEST_SMALL_MAX_RECORD_SIZE, TEST_SMALL_MAX_BATCH_SIZE, TEST_SMALL_MAX_RECORDS_IN_BATCH)
        #[["1234", "123456", "12", "123", "123456", "12"],["1234", "123456"]]
        self.assertEqual(len(response), 2, "Should be 2")

    def test_splitting2(self):
        response = batcher(self.records1, TEST_SMALL_MAX_RECORD_SIZE, TEST_SMALL_MAX_BATCH_SIZE, TEST_SMALL_MAX_RECORDS_IN_BATCH)
        #[["1234", "123456", "12", "123", "123456", "12"],["1234", "123456"]]
        self.assertEqual(len(response[0]), 6, "Should be 6")

    def test_splitting3(self):
        response = batcher(self.records1, TEST_SMALL_MAX_RECORD_SIZE, TEST_SMALL_MAX_BATCH_SIZE, TEST_SMALL_MAX_RECORDS_IN_BATCH)
        #[["1234", "123456", "12", "123", "123456", "12"],["1234", "123456"]]
        self.assertEqual(len(response[1]), 2, "Should be 2")

    def test_utf1(self):
        response = batcher([u'\u0041\u0041\u0041\u0041\u0041', u'\u0041\u0041'], TEST_SMALL_MAX_RECORD_SIZE, TEST_SMALL_MAX_BATCH_SIZE, TEST_SMALL_MAX_RECORDS_IN_BATCH)
        #[['AAAAA', 'AA']]
        self.assertEqual(len(response), 1, "Should be 1")

    def test_utf2(self):
        response = batcher([u'\u03c0\u03c0\u03c0\u03c0\u03c0', u'\u03c0\u03c0'], TEST_SMALL_MAX_RECORD_SIZE, TEST_SMALL_MAX_BATCH_SIZE, TEST_SMALL_MAX_RECORDS_IN_BATCH)
        #[['ππ']]
        self.assertEqual(len(response), 1, "Should be 1")

    def test_utf3(self):
        response = batcher([u'\u03c0\u03c0\u03c0\u03c0', u'\u03c0\u03c0'], TEST_SMALL_MAX_RECORD_SIZE, TEST_SMALL_MAX_BATCH_SIZE, TEST_SMALL_MAX_RECORDS_IN_BATCH)
        #[['ππππ', 'ππ']]
        self.assertEqual(len(response[0]), 2, "Should be 2")

    def test_max_size_1(self):
        array = []
        array.append(generate_fixed_size_record(False, 1024*1024)) 
        response = batcher(array)
        self.assertEqual(len(response), 1, "Should be 1")
        self.assertEqual(len(response[0]), 1, "Should be 1")

    def test_max_size_2(self):
        array = []
        array.append(generate_fixed_size_record(False, 1024*1024+1)) 
        response = batcher(array)
        self.assertEqual(len(response), 0, "Should be 0")

    def test_max_size_3(self):
        array = []
        array.append(generate_fixed_size_record(False, 1024*1024)) 
        array.append(generate_fixed_size_record(False, 1024*1024+1)) 
        response = batcher(array)
        self.assertEqual(len(response), 1, "Should be 1")
        self.assertEqual(len(response[0]), 1, "Should be 1")

    def test_record_order(self):
        array = []
        array.append(generate_fixed_size_record(False, 5))
        array.append(generate_fixed_size_record(False, 10))
        array.append(generate_fixed_size_record(False, 1024*1024))
        array.append(generate_fixed_size_record(False, 1024*500))
        array.append(generate_fixed_size_record(False, 1024*30))
        array.append(generate_fixed_size_record(False, 1024))
        array.append(generate_fixed_size_record(False, 321))
        array.append(generate_fixed_size_record(False, 120546))
        array.append(generate_fixed_size_record(False, 45))
        array.append(generate_fixed_size_record(False, 555555))
        response = batcher(array)
        response_generator = (record 
                for batch in response
                for record in batch
            )
        response_string = "".join(response_generator)
        array_string = ''.join([record for record in array]) 
        self.assertEqual(response_string, array_string, "Should be equal but are not")

    #TODO test maximum size of output batch

    #TODO test maximum number ot records in output batch




if __name__ == '__main__':
    unittest.main()