import unittest

from pyloggermanager import Logger, RootLogger, Registry


class TestRegistry(unittest.TestCase):
    """Unit test cases for Registry class"""

    def setUp(self) -> None:
        self.logger = Logger(name='testlogger')
        self.root_logger = RootLogger(20)

    def test_init_valid(self):
        """Test if init method initializes as expected"""
        registry = Registry(self.logger)
        expected_output = {
            self.logger: None
        }
        self.assertDictEqual(expected_output, registry.logger_map)

    def test_init_valid_root_logger(self):
        """Test if init method initializes as expected"""
        registry = Registry(self.root_logger)
        expected_output = {
            self.root_logger: None
        }
        self.assertDictEqual(expected_output, registry.logger_map)

    def test_init_invalid(self):
        """Test if init method raises TypeError"""
        with self.assertRaises(TypeError):
            Registry({'logger'})

    def test_logger_map_property_valid(self):
        """Test logger map property"""
        registry = Registry(self.logger)
        registry.logger_map = {
            self.root_logger: None
        }
        expected_output = {
            self.root_logger: None
        }
        self.assertDictEqual(expected_output, registry.logger_map)

    def test_logger_map_property_invalid(self):
        """Test if logger map raises TypeError"""
        registry = Registry(self.logger)
        with self.assertRaises(TypeError):
            registry.logger_map = 100

    def test_append_valid(self):
        """Test if the append method works as expected"""
        registry = Registry(self.logger)
        registry.append(self.root_logger)
        expected_output = {
            self.logger: None,
            self.root_logger: None
        }
        self.assertDictEqual(expected_output, registry.logger_map)

    def test_append_invalid(self):
        """Test if the append method raises TypeError"""
        registry = Registry(self.logger)
        with self.assertRaises(TypeError):
            registry.append('logger')


if __name__ == "__main__":
    unittest.main()
