import os
import unittest

import pytest

import pyloggermanager
from pyloggermanager import LogLevel, FileMode
from pyloggermanager.handlers import FileHandler
from utilityclass import UtilityClass


class TestPyLoggerManagerConfig(unittest.TestCase):
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
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(
                file_name=file_name,
                file_mode=FileMode.APPEND,
                level=LogLevel.INFO
            )
            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            self.assertEqual(FileHandler, type(logger.handlers[0]))
        finally:
            UtilityClass.delete_file(file_name)

    @pytest.mark.sequential_order
    def test_load_config_valid_no_params(self):
        """Test if load config works as expected"""
        try:
            pyloggermanager.load_config()
            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            self.assertEqual(FileHandler, type(logger.handlers[0]))
        finally:
            UtilityClass.delete_file('default.log')


if __name__ == "__main__":
    unittest.main()
