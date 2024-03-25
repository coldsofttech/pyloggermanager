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

import io
import os
import sys
import unittest

import pyloggermanager
from pyloggermanager import Logger, LogLevel
from pyloggermanager.handlers import FileHandler


class TestPyLoggerManager(unittest.TestCase):
    """Unit test cases for pyloggermanager package functions"""

    def setUp(self) -> None:
        self.logger = None
        self.exec_info = (ValueError, ValueError('Test error'), None)

    def tearDown(self) -> None:
        if self.logger is not None:
            for handler in self.logger.handlers:
                handler.close()
                if type(handler) == FileHandler:
                    try:
                        file_name = str(handler.filename)
                        os.remove(file_name)
                    except (FileNotFoundError, PermissionError, IsADirectoryError):
                        pass

        pyloggermanager.shutdown()
        self.logger = None

    def test_get_logger_valid_empty(self):
        """Test if the get logger works as expected"""
        pyloggermanager.load_config()
        self.logger = pyloggermanager.get_logger()
        self.assertEqual('root', self.logger.name)

    def test_get_logger_valid(self):
        """Test if the get logger works as expected"""
        self.logger = Logger(name='TestLogger')
        check_logger = None
        pyloggermanager.load_config()
        try:
            check_logger = pyloggermanager.get_logger('TestLogger')
            self.assertEqual('TestLogger', check_logger.name)
        finally:
            for handler in check_logger.handlers:
                handler.flush()
                handler.close()

    def test_get_logger_invalid(self):
        """Test if the get logger raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.get_logger({'logger'})

    def test_disable_valid(self):
        """Test if disable works as expected"""
        pyloggermanager.load_config()
        pyloggermanager.disable(LogLevel.WARNING)
        self.logger = pyloggermanager.get_logger()
        self.assertEqual('root', self.logger.name)
        self.assertEqual(LogLevel.WARNING, self.logger.manager.disable)

    def test_disable_invalid(self):
        """Test if disable raises TypeError"""
        pyloggermanager.load_config()
        with self.assertRaises(TypeError):
            pyloggermanager.disable('INFO')

        self.logger = pyloggermanager.get_logger()

    def test_info_valid(self):
        """Test if info works as expected"""
        pyloggermanager.load_config()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        pyloggermanager.info('Test info message', False)
        sys.stdout = sys.__stdout__
        expected_output_console = ''
        expected_output_file = ' :: INFO :: Test info message'
        self.assertIn(expected_output_console, output_buffer.getvalue())

        self.logger = pyloggermanager.get_logger()
        with open(self.logger.handlers[0].filename, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_output_file, file_content)

    def test_info_invalid_message(self):
        """Test if info raises TypeError"""
        pyloggermanager.load_config()
        with self.assertRaises(TypeError):
            pyloggermanager.info(200)

        self.logger = pyloggermanager.get_logger()

    def test_info_invalid_ignore_display(self):
        """Test if info raises TypeError"""
        pyloggermanager.load_config()
        with self.assertRaises(TypeError):
            pyloggermanager.info('Test message', ignore_display=200)

        self.logger = pyloggermanager.get_logger()

    def test_info_invalid_exec_info(self):
        """Test if info raises TypeError"""
        pyloggermanager.load_config()
        with self.assertRaises(TypeError):
            pyloggermanager.info('Test message', False, {'dict'})

        self.logger = pyloggermanager.get_logger()

    def test_info_invalid_stack_info(self):
        """Test if info raises TypeError"""
        pyloggermanager.load_config()
        with self.assertRaises(TypeError):
            pyloggermanager.info(
                'Test message', False, self.exec_info, 'dict'
            )

        self.logger = pyloggermanager.get_logger()

    def test_info_invalid_stack_level(self):
        """Test if info raises TypeError"""
        pyloggermanager.load_config()
        with self.assertRaises(TypeError):
            pyloggermanager.info(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )


if __name__ == "__main__":
    unittest.main()
