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

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import DefaultFormatter, DEFAULT_FORMAT, DATE_FORMAT


class TestDefaultFormatter(unittest.TestCase):
    """Unit test case methods for DefaultFormatter class."""

    def test_init_no_input(self):
        """Test if init method is initialized without any input."""
        formatter = DefaultFormatter()
        expected_format_str = DEFAULT_FORMAT
        expected_date_format = DATE_FORMAT
        self.assertEqual(formatter.format_str, expected_format_str)
        self.assertEqual(formatter.date_format, expected_date_format)

    def test_init_format_str_valid(self):
        """Test if init method is initialized when valid format_str is provided."""
        format_str = '%(time)s :: %(message)s'
        formatter = DefaultFormatter(format_str)
        self.assertEqual(formatter.format_str, format_str)

    def test_init_format_str_invalid(self):
        """Test if init method raises TypeError when invalid inputs are provided."""
        format_str = {
            'time': '%(time)s'
        }
        with self.assertRaises(TypeError):
            DefaultFormatter(format_str)

    def test_format_valid(self):
        """Test if format method returns output in expected format."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = DefaultFormatter()
        expected_output = (
            f'{formatter.format_time(record.time.timetuple(), formatter.date_format)} :: '
            f'WARNING :: Test message'
        )
        self.assertEqual(formatter.format(record), expected_output)

    def test_format_exec_info_empty_valid(self):
        """Test if format method returns output when empty exec_info is provided."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = DefaultFormatter('%(time)s :: %(level_name)s :: %(message)s :: %(exec_info)s')
        expected_output = (
            f'{formatter.format_time(record.time.timetuple(), formatter.date_format)} :: '
            f'WARNING :: Test message :: '
        )
        self.assertEqual(formatter.format(record), expected_output)

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
        formatter = DefaultFormatter('%(time)s :: %(level_name)s :: %(message)s :: %(exec_info)s')
        expected_output = (
            f'{formatter.format_time(record.time.timetuple(), formatter.date_format)} :: '
            f'WARNING :: Test message :: ValueError: Test error'
        )
        self.assertEqual(formatter.format(record), expected_output)

    def test_format_invalid(self):
        """Test if format method raises TypeError when invalid inputs are provided."""
        record = 100
        formatter = DefaultFormatter()
        with self.assertRaises(TypeError):
            formatter.format(record)


if __name__ == "__main__":
    unittest.main()
