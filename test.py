import unittest
from lastrun import when, record, recorder
import datetime
import os


class TestLastrun(unittest.TestCase):

    def test_first_run(self):
        self.assertEqual(when(), None)
        self.assertEqual(recorder(), None)

    def test_next_run(self):
        self.assertIsInstance(when(), datetime.datetime)
        self.assertIsInstance(recorder(), datetime.timedelta)

    @classmethod
    def tearDownClass(cls):
        os.remove('.lastrun')


if __name__ == '__main__':
    unittest.main()
