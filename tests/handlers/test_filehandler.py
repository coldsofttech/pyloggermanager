import inspect
import io
import os
import sys
import unittest

from pycolorecho import ColorMapper, TextColor, RESET, is_colorization_supported

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import Formatter
from pyloggermanager.handlers import Handler, FileHandler


class TestFileHandler(unittest.TestCase):
    """Unit test cases for FileHandler class."""

    def tearDown(self) -> None:
        handlers = Handler.get_handlers()
        for handler in handlers:
            file_name = handler.filename
            handler.close()
            try:
                os.remove(file_name)
            except (FileNotFoundError, PermissionError, IsADirectoryError):
                pass

    def test_init_no_input(self):
        """Test if init method is initialized without inputs."""
        handler = FileHandler()
        expected_name = None
        expected_level = 20
        expected_colorization = None
        expected_file_name = 'default.log'
        expected_file_mode = 'a'
        expected_encoding = 'UTF-8'
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        self.assertEqual(handler.filename, expected_file_name)
        self.assertEqual(handler.filemode, expected_file_mode)
        self.assertEqual(handler.encoding, expected_encoding)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_filename_valid(self):
        """Test if init method is initialized with valid filename input."""
        file_name = 'app.log'
        handler = FileHandler(file_name=file_name)
        expected_name = None
        expected_level = 20
        expected_colorization = None
        expected_file_mode = 'a'
        expected_encoding = 'UTF-8'
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        self.assertEqual(handler.filename, file_name)
        self.assertEqual(handler.filemode, expected_file_mode)
        self.assertEqual(handler.encoding, expected_encoding)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_filename_invalid(self):
        """Test if init raises TypeError when invalid filename is provided."""
        with self.assertRaises(TypeError):
            FileHandler(file_name={'test'})

    def test_init_filemode_valid(self):
        """Test if init method is initialized with valid filemode input."""
        file_mode = 'r'
        handler = FileHandler(file_mode=file_mode)
        expected_name = None
        expected_level = 20
        expected_colorization = None
        expected_file_name = 'default.log'
        expected_encoding = 'UTF-8'
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        self.assertEqual(handler.filename, expected_file_name)
        self.assertEqual(handler.filemode, file_mode)
        self.assertEqual(handler.encoding, expected_encoding)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_filemode_invalid(self):
        """Test if init raises TypeError when invalid filemode is provided."""
        with self.assertRaises(TypeError):
            FileHandler(file_mode=100)

    def test_init_filemode_do_not_exist(self):
        """Test if init raises ValueError when filemode that do not exist is provided."""
        with self.assertRaises(ValueError):
            FileHandler(file_mode='c')

    def test_init_encoding_valid(self):
        """Test if init method is initialized with valid encoding input."""
        encoding = 'ANSI'
        handler = FileHandler(encoding=encoding)
        expected_name = None
        expected_level = 20
        expected_colorization = None
        expected_file_name = 'default.log'
        expected_file_mode = 'a'
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        self.assertEqual(handler.filename, expected_file_name)
        self.assertEqual(handler.filemode, expected_file_mode)
        self.assertEqual(handler.encoding, encoding)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_encoding_invalid(self):
        """Test if init raises TypeError when invalid encoding is provided."""
        with self.assertRaises(TypeError):
            FileHandler(encoding=100)

    def test_filename_property_valid(self):
        """Test if filename property returns expected value."""
        handler = FileHandler()
        file_name = 'app.log'
        handler.filename = file_name
        self.assertEqual(handler.filename, file_name)

    def test_filename_property_invalid(self):
        """Test is filename property raises TypeError when invalid value is provided."""
        handler = FileHandler()
        file_name = 100
        with self.assertRaises(TypeError):
            handler.filename = file_name

    def test_filemode_property_valid(self):
        """Test if filemode property returns expected value."""
        handler = FileHandler()
        file_mode = 'r'
        handler.filemode = file_mode
        self.assertEqual(handler.filemode, file_mode)

    def test_filemode_property_invalid(self):
        """Test is filemode property raises TypeError when invalid value is provided."""
        handler = FileHandler()
        file_mode = 100
        with self.assertRaises(TypeError):
            handler.filemode = file_mode

    def test_filemode_property_do_not_exist(self):
        """Test if filemode property raises ValueError when mode that do not exist is provided."""
        handler = FileHandler()
        file_mode = 'c'
        with self.assertRaises(ValueError):
            handler.filemode = file_mode

    def test_encoding_property_valid(self):
        """Test if encoding property returns expected value."""
        handler = FileHandler()
        encoding = 'ANSI'
        handler.encoding = encoding
        self.assertEqual(handler.encoding, encoding)

    def test_encoding_property_invalid(self):
        """Test is encoding property raises TypeError when invalid value is provided."""
        handler = FileHandler()
        encoding = 100
        with self.assertRaises(TypeError):
            handler.encoding = encoding

    def test_close(self):
        """Test close method"""
        handler = FileHandler()
        handler.close()

    def test_emit_valid_no_colorization(self):
        """Test if emit method prints message as expected."""
        file_name = 'valnocol.log'
        handler = FileHandler(file_name=file_name)
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        handler.emit(record, False)
        sys.stdout = sys.__stdout__
        expected_console_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test message\n'
        )
        self.assertEqual(output_buffer.getvalue(), expected_console_output)

        expected_file_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test message'
        )
        with open(file_name, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_file_output, file_content)

    def test_emit_valid_colorization(self):
        """Test if emit method prints message as expected."""
        file_name = 'valcol1.log'
        handler = FileHandler(file_name=file_name)
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test error message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        colorization = ColorMapper()
        colorization.add_mapping('error', ['error'], text_color=TextColor.RED)
        handler.colorization = colorization
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        handler.emit(record, False)
        sys.stdout = sys.__stdout__
        expected_console_output = (
            f'{TextColor.RED}'
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
            f'{RESET}\n'
        ) if is_colorization_supported() else (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
            f'\n'
        )
        self.assertEqual(repr(output_buffer.getvalue()), repr(expected_console_output))

        expected_file_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
        )
        with open(file_name, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_file_output, file_content)

    def test_emit_valid_colorization_no_display(self):
        """Test if emit method prints message as expected."""
        file_name = 'valcol2.log'
        handler = FileHandler(file_name=file_name)
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test error message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        colorization = ColorMapper()
        colorization.add_mapping('error', ['error'], text_color=TextColor.RED)
        handler.colorization = colorization
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        handler.emit(record, True)
        sys.stdout = sys.__stdout__
        expected_output = ''
        self.assertEqual(repr(output_buffer.getvalue()), repr(expected_output))

        expected_file_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
        )
        with open(file_name, 'r') as file:
            file_content = file.read()
            self.assertIn(expected_file_output, file_content)

    def test_emit_invalid(self):
        """Test if emit method raises TypeError when invalid inputs are provided."""
        handler = FileHandler()
        record = 100
        with self.assertRaises(TypeError):
            handler.emit(record, 100)

    def test_flush(self):
        """Test flush method."""
        handler = FileHandler()
        handler.flush()


if __name__ == "__main__":
    unittest.main()
