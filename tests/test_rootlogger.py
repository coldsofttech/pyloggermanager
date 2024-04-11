import unittest

from pyloggermanager import RootLogger


class TestRootLogger(unittest.TestCase):
    """Unit test cases for RootLogger class"""

    def test_init_valid(self):
        """Test if init method initializes as expected"""
        root_logger = RootLogger(20)
        self.assertEqual('root', root_logger.name)
        self.assertEqual(20, root_logger.level)

    def test_init_invalid(self):
        """Test if init method raises TypeError"""
        with self.assertRaises(TypeError):
            RootLogger('level 20')


if __name__ == "__main__":
    unittest.main()
