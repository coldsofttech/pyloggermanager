import inspect
import time
import unittest
from datetime import datetime
from unittest.mock import ANY

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import DEFAULT_FORMAT, CSV_FORMAT, JSON_FORMAT, DATE_FORMAT, Formatter


class TestFormatter(unittest.TestCase):
    """Unit test cases for Formatter class"""

    def test_default_format_property(self):
        """Test if default format property returns expected value."""
        expected_value = '%(time)s :: %(level_name)s :: %(message)s'
        actual_value = DEFAULT_FORMAT
        self.assertEqual(actual_value, expected_value)

    def test_csv_format_property(self):
        """Test if csv format property returns expected value."""
        expected_value = '%(time)s,%(level_name)s,%(message)s'
        actual_value = CSV_FORMAT
        self.assertEqual(actual_value, expected_value)

    def test_json_format_property(self):
        """Test if json format property returns expected value."""
        expected_value = {
            "time": "%(time)s",
            "levelName": "%(level_name)s",
            "message": "%(message)s"
        }
        actual_value = JSON_FORMAT
        self.assertDictEqual(actual_value, expected_value)

    def test_date_format_property(self):
        """Test if date format property returns expected value."""
        expected_value = '%Y-%m-%d %H:%M:%S'
        actual_value = DATE_FORMAT
        self.assertEqual(actual_value, expected_value)

    def test_init_no_input(self):
        """Test if init method is initiated without any inputs."""
        formatter = Formatter()
        expected_format_str = DEFAULT_FORMAT
        expected_date_format = DATE_FORMAT
        self.assertEqual(formatter.format_str, expected_format_str)
        self.assertEqual(formatter.date_format, expected_date_format)

    def test_init_valid_format_str(self):
        """Test if init method is initiated when valid format_str is provided."""
        format_str = '%(time)s :: %(message)s'
        formatter = Formatter(format_str)
        self.assertEqual(formatter.format_str, format_str)

    def test_init_valid_format_dict(self):
        """Test if init method is initiated when valid format_str is provided."""
        format_dict = {
            'time': '%(time)s',
            'message': '%(message)s'
        }
        formatter = Formatter(format_dict)
        self.assertDictEqual(formatter.format_str, format_dict)

    def test_init_date_format(self):
        """Test if init method is initiated when valid date_format is provided."""
        date_format = '%Y-%m-%d'
        formatter = Formatter(date_format=date_format)
        self.assertEqual(formatter.date_format, date_format)

    def test_init_invalid(self):
        """Test if init method raises TypeError when invalid inputs are provided."""
        format_str = 100
        date_format = {'test'}
        with self.assertRaises(TypeError):
            Formatter(format_str, date_format)

    def test_date_format_property_valid(self):
        """Test if date format property returns valid value."""
        date_format = '%Y-%m-%d'
        formatter = Formatter()
        formatter.date_format = date_format
        self.assertEqual(formatter.date_format, date_format)

    def test_date_format_property_invalid(self):
        """Test if date format raises TypeError when invalid value is provided."""
        date_format = 100
        formatter = Formatter()
        with self.assertRaises(TypeError):
            formatter.date_format = date_format

    def test_format_str_property_valid(self):
        """Test if format str property returns valid value."""
        format_str = '%(time)s :: %(message)s'
        formatter = Formatter()
        formatter.format_str = format_str
        self.assertEqual(formatter.format_str, format_str)

    def test_format_dict_property_valid(self):
        """Test if format str property accepts dict value."""
        format_dict = {
            'loggedTime': '%(time)s'
        }
        formatter = Formatter()
        formatter.format_str = format_dict
        self.assertDictEqual(formatter.format_str, format_dict)

    def test_format_str_property_invalid(self):
        """Test if format str raises TypeError property when invalid input is provided."""
        format_str = 100
        formatter = Formatter()
        with self.assertRaises(TypeError):
            formatter.format_str = format_str

    def test_format(self):
        """Test if format method raises NotImplementedError."""
        formatter = Formatter()
        with self.assertRaises(NotImplementedError):
            formatter.format(None)

    def test_format_time_valid(self):
        """Test if format time returns expected value."""
        formatter = Formatter()
        current_date = datetime.utcnow()
        current_date_tuple = current_date.timetuple()
        expected_output = time.strftime(formatter.date_format, current_date_tuple)
        self.assertEqual(formatter.format_time(current_date_tuple, formatter.date_format), expected_output)

    def test_format_time_invalid(self):
        """Test if format time raises TypeError when invalid inputs are provided."""
        formatter = Formatter()
        with self.assertRaises(TypeError):
            formatter.format_time(100, {'dict'})

    def test_format_exception(self):
        """Test if format exception returns '' when no inputs are provided."""
        formatter = Formatter()
        self.assertEqual(formatter.format_exception(), '')

    def test_format_exception_valid(self):
        """Test if format exception returns valid value when exec_info is provided."""
        exec_info = (ValueError, ValueError('Test error'), None)
        formatter = Formatter()
        expected_output = 'ValueError: Test error'
        self.assertEqual(formatter.format_exception(exec_info), expected_output)

    def test_format_exception_invalid(self):
        """Test if format exception raises TypeError when invalid inputs are provided."""
        exec_info = [ValueError, ValueError('Test error'), None]
        formatter = Formatter()
        with self.assertRaises(TypeError):
            formatter.format_exception(exec_info)

    def test__log_attributes_valid(self):
        """Test if _log attributes returns expected values."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = Formatter()
        expected_output = {
            '%(time)s': ANY,
            '%(message)s': 'Test message',
            '%(logger_name)s': 'TestLogger',
            '%(level_name)s': 'WARNING',
            '%(level_number)d': 30,
            '%(file_name)s': 'test_formatter',
            '%(class_name)s': 'TestFormatter',
            '%(function_name)s': 'test__log_attributes_valid',
            '%(module_name)s': 'test_formatter',
            '%(path_name)s': ANY,
            '%(exec_info)s': '',
            '%(stack_info)s': None,
            '%(thread)d': ANY,
            '%(thread_name)s': 'MainThread',
            '%(process_id)d': ANY
        }
        actual_output = formatter._log_attributes(record, formatter.date_format)

        for key, expected_value in expected_output.items():
            actual_value = actual_output.get(key, '')

            if key == '%(time)s':
                try:
                    datetime.strptime(actual_value, formatter.date_format)
                except ValueError:
                    raise AssertionError(
                        f'Expected "%(time)s" to be in format "{formatter.date_format}", but got "{actual_value}"'
                    )
            elif key == '%(path_name)s':
                assert actual_value.endswith('test_formatter.py')
            else:
                assert actual_value == expected_value

    def test__log_attributes_valid_exec_info(self):
        """Test if _log attributes returns expected values when exec_info is passed."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        exec_info = (ValueError, ValueError('Test error'), None)
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame,
            exec_info=exec_info
        )
        formatter = Formatter()
        expected_output = {
            '%(time)s': ANY,
            '%(message)s': 'Test message',
            '%(logger_name)s': 'TestLogger',
            '%(level_name)s': 'WARNING',
            '%(level_number)d': 30,
            '%(file_name)s': 'test_formatter',
            '%(class_name)s': 'TestFormatter',
            '%(function_name)s': 'test__log_attributes_valid_exec_info',
            '%(module_name)s': 'test_formatter',
            '%(path_name)s': ANY,
            '%(exec_info)s': 'ValueError: Test error',
            '%(stack_info)s': None,
            '%(thread)d': ANY,
            '%(thread_name)s': 'MainThread',
            '%(process_id)d': ANY
        }
        actual_output = formatter._log_attributes(record, formatter.date_format)

        for key, expected_value in expected_output.items():
            actual_value = actual_output.get(key, '')

            if key == '%(time)s':
                try:
                    datetime.strptime(actual_value, formatter.date_format)
                except ValueError:
                    raise AssertionError(
                        f'Expected "%(time)s" to be in format "{formatter.date_format}", but got "{actual_value}"'
                    )
            elif key == '%(path_name)s':
                assert actual_value.endswith('test_formatter.py')
            else:
                assert actual_value == expected_value

    def test__log_attributes_invalid(self):
        """Test if _log attributes raises TypeError when invalid inputs are passed."""
        record = 100
        formatter = Formatter()
        with self.assertRaises(TypeError):
            formatter._log_attributes(record, {'dict'})


if __name__ == "__main__":
    unittest.main()
