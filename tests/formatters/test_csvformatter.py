import inspect
import unittest

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import CSVFormatter, CSV_FORMAT, DATE_FORMAT


class TestCSVFormatter(unittest.TestCase):
    """Unit test case methods for CSVFormatter class."""

    def test_init_no_input(self):
        """Test if init method is initialized without any input."""
        formatter = CSVFormatter()
        expected_format_str = CSV_FORMAT
        expected_date_format = DATE_FORMAT
        self.assertEqual(formatter.format_str, expected_format_str)
        self.assertEqual(formatter.date_format, expected_date_format)

    def test_init_format_str_valid(self):
        """Test if init method is initialized when valid format_str is provided."""
        format_str = '%(time)s,%(message)s'
        formatter = CSVFormatter(format_str)
        self.assertEqual(formatter.format_str, format_str)

    def test_init_format_str_invalid(self):
        """Test if init method raises TypeError when invalid inputs are provided."""
        format_str = {
            'time': '%(time)s'
        }
        with self.assertRaises(TypeError):
            CSVFormatter(format_str)

    def test_init_format_str_invalid_csv_format(self):
        """Test if init method raises ValueError when invalid csv input is provided."""
        format_str = '%(time)s :: %(level_name)s :: %(message)s'
        with self.assertRaises(ValueError):
            CSVFormatter(format_str)

    def test_format_valid(self):
        """Test if format method returns output in expected format."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = CSVFormatter()
        expected_output = (
            f'{formatter.format_time(record.time.timetuple(), formatter.date_format)},'
            f'WARNING,Test message'
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
        formatter = CSVFormatter('%(time)s,%(level_name)s,%(message)s,%(exec_info)s')
        expected_output = (
            f'{formatter.format_time(record.time.timetuple(), formatter.date_format)},'
            f'WARNING,Test message,'
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
        formatter = CSVFormatter('%(time)s,%(level_name)s,%(message)s,%(exec_info)s')
        expected_output = (
            f'{formatter.format_time(record.time.timetuple(), formatter.date_format)},'
            f'WARNING,Test message,ValueError: Test error'
        )
        self.assertEqual(formatter.format(record), expected_output)

    def test_format_invalid(self):
        """Test if format method raises TypeError when invalid inputs are provided."""
        record = 100
        formatter = CSVFormatter()
        with self.assertRaises(TypeError):
            formatter.format(record)


if __name__ == "__main__":
    unittest.main()
