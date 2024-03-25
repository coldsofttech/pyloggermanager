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

import inspect
import unittest
from datetime import datetime
from unittest.mock import ANY

from pyloggermanager import CallerFrame, Record, LogLevel


class TestRecord(unittest.TestCase):
    """Unit test cases for Record class."""

    def setUp(self) -> None:
        self.caller_frame = CallerFrame.get_caller_details(inspect.currentframe())
        self.record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=20,
            caller_frame=self.caller_frame,
            exec_info=(ValueError, ValueError('Test error'), None)
        )

    def tearDown(self) -> None:
        self.record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=20,
            caller_frame=self.caller_frame,
            exec_info=(ValueError, ValueError('Test error'), None)
        )

    def test_init_valid(self):
        """Test if init method initializes all the required variables."""
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=20,
            caller_frame=self.caller_frame
        )
        assert isinstance(record.time, datetime)
        self.assertEqual(record.message, 'Test message')
        self.assertEqual(record.logger_name, 'TestLogger')
        self.assertEqual(record.level_number, 20)
        self.assertEqual(record.level_name, LogLevel.get_level(20))
        self.assertEqual(record.file_name, 'test_record')
        self.assertEqual(record.class_name, 'TestRecord')
        self.assertEqual(record.function_name, 'setUp')
        self.assertEqual(record.module_name, 'test_record')
        assert record.path_name.endswith('test_record.py')
        self.assertEqual(record.exec_info, None)
        self.assertEqual(record.stack_info, None)
        assert isinstance(record.thread, int)
        self.assertEqual(record.thread_name, 'MainThread')
        assert isinstance(record.process_id, int)

    def test_init_invalid_message(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Record(
                message=100,
                logger_name='TestLogger',
                level_number=20,
                caller_frame=self.caller_frame
            )

    def test_init_invalid_logger_name(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Record(
                message='Test message',
                logger_name=100,
                level_number=20,
                caller_frame=self.caller_frame
            )

    def test_init_invalid_level(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Record(
                message='Test message',
                logger_name='TestLogger',
                level_number='INFO',
                caller_frame=self.caller_frame
            )

    def test_init_invalid_caller_frame(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Record(
                message='Test message',
                logger_name='TestLogger',
                level_number=20,
                caller_frame={'dict'}
            )

    def test_init_invalid_exec_info(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Record(
                message='Test message',
                logger_name='TestLogger',
                level_number=20,
                caller_frame=self.caller_frame,
                exec_info=[ValueError, ValueError('Test error'), None]
            )

    def test_init_invalid_stack_info(self):
        """Test if init raises TypeError when invalid inputs are provided."""
        with self.assertRaises(TypeError):
            Record(
                message='Test message',
                logger_name='TestLogger',
                level_number=20,
                caller_frame=self.caller_frame,
                stack_info=100
            )

    def test_time_property(self):
        """Test time property"""
        assert isinstance(self.record.time, datetime)

    def test_message_property_valid(self):
        """Test message property"""
        self.record.message = 'Test error message'
        self.assertEqual(self.record.message, 'Test error message')

    def test_message_property_invalid(self):
        """Test if message property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.message = 10

    def test_logger_name_property_valid(self):
        """Test logger name property"""
        self.record.logger_name = 'TestErrorLogger'
        self.assertEqual(self.record.logger_name, 'TestErrorLogger')

    def test_logger_name_property_invalid(self):
        """Test if logger name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.logger_name = 10

    def test_level_number_property_valid(self):
        """Test level number property"""
        self.record.level_number = 30
        self.assertEqual(self.record.level_number, 30)

    def test_level_number_property_invalid(self):
        """Test if level number property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.level_number = 'CUSTOM LEVEL'

    def test_level_name_property(self):
        """Test level name property"""
        self.assertEqual(self.record.level_name, 'INFO')

    def test_file_name_property_valid(self):
        """Test file name property"""
        self.record.file_name = 'TestFileName'
        self.assertEqual(self.record.file_name, 'TestFileName')

    def test_file_name_property_invalid(self):
        """Test if file name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.file_name = 10

    def test_class_name_property_valid(self):
        """Test class name property"""
        self.record.class_name = 'TestClass'
        self.assertEqual(self.record.class_name, 'TestClass')

    def test_class_name_property_invalid(self):
        """Test if class name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.class_name = 100

    def test_function_name_property_valid(self):
        """Test function name property"""
        self.record.function_name = 'TestFunction'
        self.assertEqual(self.record.function_name, 'TestFunction')

    def test_function_name_property_invalid(self):
        """Test if function name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.function_name = 100

    def test_module_name_property_valid(self):
        """Test module name property"""
        self.record.module_name = 'TestModule'
        self.assertEqual(self.record.module_name, 'TestModule')

    def test_module_name_property_invalid(self):
        """Test if module name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.module_name = 100

    def test_path_name_property_valid(self):
        """Test path name property"""
        self.record.path_name = 'TestPath'
        self.assertEqual(self.record.path_name, 'TestPath')

    def test_path_name_property_invalid(self):
        """Test if path name property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.path_name = 100

    def test_exec_info_property_valid(self):
        """Test exec info property"""
        expected_exec_info = (TypeError, TypeError('Test error'), None)
        self.record.exec_info = expected_exec_info
        actual_exec_info = self.record.exec_info

        # Compare each element individually
        self.assertEqual(expected_exec_info[0], actual_exec_info[0])
        self.assertEqual(str(expected_exec_info[1]), str(actual_exec_info[1]))
        self.assertEqual(expected_exec_info[2], actual_exec_info[2])

    def test_exec_info_property_invalid(self):
        """Test if exec info property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.exec_info = 100

    def test_stack_info_property_valid(self):
        """Test stack info property"""
        self.record.stack_info = 'TestStack'
        self.assertEqual(self.record.stack_info, 'TestStack')

    def test_stack_info_property_invalid(self):
        """Test if stack info property raises TypeError"""
        with self.assertRaises(TypeError):
            self.record.stack_info = 100

    def test_thread_property(self):
        """Test thread property"""
        assert isinstance(self.record.thread, int)

    def test_thread_name_property(self):
        """Test thread name property"""
        self.assertEqual(self.record.thread_name, 'MainThread')

    def test_process_id_property(self):
        """Test process id property"""
        assert isinstance(self.record.process_id, int)

    def test_to_dict(self):
        """Test to dict returns as expected"""
        expected_output = {
            'time': ANY,
            'message': 'Test message',
            'logger_name': 'TestLogger',
            'level_name': 'INFO',
            'level_number': 20,
            'file_name': 'test_record',
            'class_name': 'TestRecord',
            'function_name': 'setUp',
            'module_name': 'test_record',
            'path_name': ANY,
            'exec_info': ANY,
            'stack_info': None,
            'thread': ANY,
            'thread_name': 'MainThread',
            'process_id': ANY
        }
        actual_output = self.record.to_dict()

        for key, expected_value in expected_output.items():
            actual_value = actual_output.get(key, '')

            if key == '%(time)s':
                assert isinstance(actual_value, datetime)
            elif key == '%(path_name)s':
                assert actual_value.endswith('test_record.py')
            else:
                assert actual_value == expected_value

    def test_to_json(self):
        """Test to json works as expected"""
        expected_output = {
            'time': ANY,
            'message': 'Test message',
            'logger_name': 'TestLogger',
            'level_name': 'INFO',
            'level_number': 20,
            'file_name': 'test_record',
            'class_name': 'TestRecord',
            'function_name': 'setUp',
            'module_name': 'test_record',
            'path_name': ANY,
            'exec_info': ANY,
            'stack_info': None,
            'thread': ANY,
            'thread_name': 'MainThread',
            'process_id': ANY
        }
        actual_output = self.record.to_dict()

        for key, expected_value in expected_output.items():
            actual_value = actual_output.get(key, '')

            if key == '%(time)s':
                assert isinstance(actual_value, datetime)
            elif key == '%(path_name)s':
                assert actual_value.endswith('test_record.py')
            else:
                assert actual_value == expected_value


if __name__ == "__main__":
    unittest.main()
