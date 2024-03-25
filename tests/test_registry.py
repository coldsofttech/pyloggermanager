# Copyright (c) 2024 coldsofttech
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
