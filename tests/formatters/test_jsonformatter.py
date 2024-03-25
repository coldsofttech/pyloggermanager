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
import json
import unittest

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import JSONFormatter, JSON_FORMAT, DATE_FORMAT


class TestJSONFormatter(unittest.TestCase):
    """Unit test case methods for JSONFormatter class."""

    def test_init_no_input(self):
        """Test if init method is initialized without any input."""
        formatter = JSONFormatter()
        expected_format_str = JSON_FORMAT
        expected_date_format = DATE_FORMAT
        self.assertEqual(formatter.format_str, expected_format_str)
        self.assertEqual(formatter.date_format, expected_date_format)

    def test_init_format_dict_valid(self):
        """Test if init method is initialized when valid format_str is provided."""
        format_dict = {
            'time': '%(time)s',
            'message': '%(message)s'
        }
        formatter = JSONFormatter(format_dict)
        self.assertDictEqual(formatter.format_str, format_dict)

    def test_init_format_dict_invalid(self):
        """Test if init method raises TypeError when invalid inputs are provided."""
        format_str = '%(time)s :: %(message)s'
        with self.assertRaises(TypeError):
            JSONFormatter(format_str)

    def test_format_valid(self):
        """Test if format method returns output in expected format."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = JSONFormatter()
        expected_output = {
            'time': f'{formatter.format_time(record.time.timetuple(), formatter.date_format)}',
            'levelName': 'WARNING',
            'message': 'Test message'
        }
        expected_output_json_str = json.dumps(expected_output, indent=4)
        self.assertEqual(formatter.format(record), expected_output_json_str)

    def test_format_exec_info_empty_valid(self):
        """Test if format method returns output when empty exec_info is provided."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        format_dict = {
            'time': '%(time)s',
            'levelName': '%(level_name)s',
            'message': '%(message)s',
            'execInfo': '%(exec_info)s'
        }
        formatter = JSONFormatter(format_dict)
        expected_output = {
            'time': f'{formatter.format_time(record.time.timetuple(), formatter.date_format)}',
            'levelName': 'WARNING',
            'message': 'Test message',
            'execInfo': ''
        }
        expected_output_json_str = json.dumps(expected_output, indent=4)
        self.assertEqual(formatter.format(record), expected_output_json_str)

    def test_format_exec_info_valid(self):
        """Test if format method returns output when exec_info is provided."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame,
            exec_info=(ValueError, ValueError('Test error'), None)
        )
        format_dict = {
            'time': '%(time)s',
            'levelName': '%(level_name)s',
            'message': '%(message)s',
            'execInfo': '%(exec_info)s'
        }
        formatter = JSONFormatter(format_dict)
        expected_output = {
            'time': f'{formatter.format_time(record.time.timetuple(), formatter.date_format)}',
            'levelName': 'WARNING',
            'message': 'Test message',
            'execInfo': 'ValueError: Test error'
        }
        expected_output_json_str = json.dumps(expected_output, indent=4)
        self.assertEqual(formatter.format(record), expected_output_json_str)

    def test_format_invalid(self):
        """Test if format method raises TypeError when invalid inputs are provided."""
        record = 100
        formatter = JSONFormatter()
        with self.assertRaises(TypeError):
            formatter.format(record)


if __name__ == "__main__":
    unittest.main()
