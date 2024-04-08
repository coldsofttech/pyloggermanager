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

import os
import unittest

import pytest

import pyloggermanager
from pyloggermanager import LogLevel, FileMode
from pyloggermanager.handlers import FileHandler
from utilityclass import UtilityClass


class TestPyLoggerManagerConfig(unittest.TestCase):
    @staticmethod
    def cleanup(logger):
        """Clean up method"""
        for handler in logger.handlers:
            handler.close()
            if handler is FileHandler:
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
    def test_load_config_invalid_file_name(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(file_name=100)

    @pytest.mark.sequential_order
    def test_load_config_invalid_file_mode(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(file_mode=100)

    @pytest.mark.sequential_order
    def test_load_config_invalid_level(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(level='INFO')

    @pytest.mark.sequential_order
    def test_load_config_invalid_format_str(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(format_str={'format_str'})

    @pytest.mark.sequential_order
    def test_load_config_invalid_date_format(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(date_format=100)

    @pytest.mark.sequential_order
    def test_load_config_invalid_stream(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(stream='stream')

    @pytest.mark.sequential_order
    def test_load_config_invalid_handlers(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(handlers='handler')

    @pytest.mark.sequential_order
    def test_load_config_invalid_colorization(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(colorization='RED')

    @pytest.mark.sequential_order
    def test_load_config_invalid_encoding(self):
        """Test if load config raises TypeError"""
        with self.assertRaises(TypeError):
            pyloggermanager.load_config(encoding=100)

    @pytest.mark.sequential_order
    def test_load_config_valid_file_name(self):
        """Test if load config works as expected"""
        try:
            file_name = UtilityClass.generate_name()
            pyloggermanager.load_config(
                file_name=file_name,
                file_mode=FileMode.APPEND,
                level=LogLevel.INFO
            )
            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            self.assertEqual(FileHandler, type(logger.handlers[0]))
        finally:
            self.cleanup(pyloggermanager.get_logger())

    @pytest.mark.sequential_order
    def test_load_config_valid_no_params(self):
        """Test if load config works as expected"""
        try:
            pyloggermanager.load_config()
            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            self.assertEqual(FileHandler, type(logger.handlers[0]))
        finally:
            self.cleanup(pyloggermanager.get_logger())


if __name__ == "__main__":
    unittest.main()
