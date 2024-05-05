import io
import sys
import unittest

import pytest

import pyloggermanager
from utilityclass import UtilityClass


class TestPyLoggerManagerError(unittest.TestCase):
    def setUp(self) -> None:
        self.exec_info = (ValueError, ValueError('Test error'), None)

    def tearDown(self) -> None:
        pyloggermanager.shutdown()

    @pytest.mark.sequential_order
    def test_error_valid(self):
        """Test if error works as expected"""
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(file_name=file_name, level=20)
            output_buffer = io.StringIO()
            sys.stdout = output_buffer
            pyloggermanager.error('Test error message', False)
            sys.stdout = sys.__stdout__
            expected_output_console = ' :: ERROR :: Test error message'
            expected_output_file = ' :: ERROR :: Test error message'
            self.assertIn(expected_output_console, output_buffer.getvalue())

            logger = pyloggermanager.get_logger()
            self.assertEqual('root', logger.name)
            with open(logger.handlers[0].filename, 'r') as file:
                file_content = file.read()
                self.assertIn(expected_output_file, file_content)
        finally:
            UtilityClass.delete_file(file_name)

    @pytest.mark.sequential_order
    def test_error_invalid_message(self):
        """Test if error raises TypeError"""
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(file_name=file_name, level=20)
            with self.assertRaises(TypeError):
                pyloggermanager.error(200)
        finally:
            UtilityClass.delete_file(file_name)

    @pytest.mark.sequential_order
    def test_error_invalid_ignore_display(self):
        """Test if error raises TypeError"""
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(file_name=file_name, level=20)
            with self.assertRaises(TypeError):
                pyloggermanager.error('Test message', ignore_display=200)
        finally:
            UtilityClass.delete_file(file_name)

    @pytest.mark.sequential_order
    def test_error_invalid_exec_error(self):
        """Test if error raises TypeError"""
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(file_name=file_name, level=20)
            with self.assertRaises(TypeError):
                pyloggermanager.error('Test message', False, {'dict'})
        finally:
            UtilityClass.delete_file(file_name)

    @pytest.mark.sequential_order
    def test_error_invalid_stack_error(self):
        """Test if error raises TypeError"""
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(file_name=file_name, level=20)
            with self.assertRaises(TypeError):
                pyloggermanager.error(
                    'Test message', False, self.exec_info, 'dict'
                )
        finally:
            UtilityClass.delete_file(file_name)

    @pytest.mark.sequential_order
    def test_error_invalid_stack_level(self):
        """Test if error raises TypeError"""
        file_name = UtilityClass.generate_name()
        try:
            pyloggermanager.load_config(file_name=file_name, level=20)
            with self.assertRaises(TypeError):
                pyloggermanager.error(
                    'Test message', False, self.exec_info, 'Stackerror', 'level'
                )
        finally:
            UtilityClass.delete_file(file_name)


if __name__ == "__main__":
    unittest.main()
