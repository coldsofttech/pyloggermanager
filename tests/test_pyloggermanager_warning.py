import io
import os
import sys
import unittest

import pytest

import pyloggermanager
from pyloggermanager.handlers import FileHandler
from utilityclass import UtilityClass


class TestPyLoggerManagerWarning(unittest.TestCase):
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
    def test_warning_valid(self):
        """Test if warning works as expected"""
        try:
            file_name = UtilityClass.generate_name()
            pyloggermanager.load_config(file_name=file_name, level=20)
            output_buffer = io.StringIO()
            sys.stdout = output_buffer
            pyloggermanager.warning('Test warning message', False)
            sys.stdout = sys.__stdout__
            expected_output_console = ' :: WARNING :: Test warning message'
            expected_output_file = ' :: WARNING :: Test warning message'
            self.assertIn(expected_output_console, output_buffer.getvalue())

            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            with open(logger.handlers[0].filename, 'r') as file:
                file_content = file.read()
                self.assertIn(expected_output_file, file_content)
        finally:
            self.cleanup(pyloggermanager.get_logger())

    @pytest.mark.sequential_order
    def test_warning_invalid_message(self):
        """Test if warning raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.warning(200)

    @pytest.mark.sequential_order
    def test_warning_invalid_ignore_display(self):
        """Test if warning raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.warning('Test message', ignore_display=200)

    @pytest.mark.sequential_order
    def test_warning_invalid_exec_info(self):
        """Test if warning raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.warning('Test message', False, {'dict'})

    @pytest.mark.sequential_order
    def test_warning_invalid_stack_info(self):
        """Test if warning raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.warning(
                'Test message', False, self.exec_info, 'dict'
            )

    @pytest.mark.sequential_order
    def test_warning_invalid_stack_level(self):
        """Test if warning raises TypeError"""
        file_name = UtilityClass.generate_name()
        pyloggermanager.load_config(file_name=file_name, level=20)
        with self.assertRaises(TypeError):
            pyloggermanager.warning(
                'Test message', False, self.exec_info, 'StackInfo', 'level'
            )


if __name__ == "__main__":
    unittest.main()
