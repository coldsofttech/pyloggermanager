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

import pytest

import pyloggermanager
from pyloggermanager.handlers import FileHandler
from utilityclass import UtilityClass


class TestPyLoggerManagerCritical(unittest.TestCase):
    @staticmethod
    def cleanup(logger):
        """Clean up method"""
        for handler in logger.handlers:
            handler.close()
            if type(handler) == FileHandler:
                try:
                    file_name = str(handler.filename)
                    os.remove(file_name)
                except (FileNotFoundError, PermissionError, IsADirectoryError):
                    pass

    def setUp(self) -> None:
        self.exec_info = (ValueError, ValueError('Test error'), None)

    def tearDown(self) -> None:
        pyloggermanager.shutdown()

    @pytest.mark.sequential_order
    def test_critical_valid(self):
        """Test if critical works as expected"""
        try:
            file_name = UtilityClass.generate_name()
            pyloggermanager.load_config(file_name=file_name, level=20)
            output_buffer = io.StringIO()
            sys.stdout = output_buffer
            pyloggermanager.critical('Test critical message', False)
            sys.stdout = sys.__stdout__
            expected_output_console = ' :: CRITICAL :: Test critical message'
            expected_output_file = ' :: CRITICAL :: Test critical message'
            self.assertIn(expected_output_console, output_buffer.getvalue())

            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            with open(logger.handlers[0].filename, 'r') as file:
                file_content = file.read()
                self.assertIn(expected_output_file, file_content)
        finally:
            self.cleanup(pyloggermanager.get_logger())

    @pytest.mark.sequential_order
    def test_critical_invalid_message(self):
        """Test if critical raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.critical(200)

    @pytest.mark.sequential_order
    def test_critical_invalid_ignore_display(self):
        """Test if critical raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.critical('Test message', ignore_display=200)

    @pytest.mark.sequential_order
    def test_critical_invalid_exec_info(self):
        """Test if critical raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.critical('Test message', False, {'dict'})

    @pytest.mark.sequential_order
    def test_critical_invalid_stack_info(self):
        """Test if critical raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.critical(
                'Test message', False, self.exec_info, 'dict'
            )

    @pytest.mark.sequential_order
    def test_critical_invalid_stack_level(self):
        """Test if critical raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.critical(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )


if __name__ == "__main__":
    unittest.main()
