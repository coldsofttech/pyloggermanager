import unittest

from pyloggermanager.streams import Stream


class TestStream(unittest.TestCase):
    """Unit test cases for Stream class"""

    def test_write(self):
        """
        Test if NotImplementedError is raised.
        """
        stream = Stream()
        with self.assertRaises(NotImplementedError):
            stream.write('message')

    def test_flush(self):
        """
        Test if NotImplementedError is raised
        """
        stream = Stream()
        with self.assertRaises(NotImplementedError):
            stream.flush()


if __name__ == "__main__":
    unittest.main()
