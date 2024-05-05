import inspect
import io
import sys
import unittest

from pycolorecho import ColorMapper, TextColor

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import Formatter
from pyloggermanager.handlers import Handler, StreamHandler
from pyloggermanager.streams import Stream, StderrStream


class TestStreamHandler(unittest.TestCase):
    """Unit test cases for StreamHandler class."""

    def tearDown(self) -> None:
        handlers = Handler.get_handlers()
        for handler in handlers:
            handler.close()

    def test_init_no_input(self):
        """Test if init method is initialized without inputs."""
        handler = StreamHandler()
        expected_name = None
        expected_level = 20
        expected_colorization = None
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)
        assert issubclass(type(handler.stream), Stream)

    def test_init_stream_valid(self):
        """Test if init method is initialized with valid stream input."""
        stream = StderrStream()
        handler = StreamHandler(stream=stream)
        expected_name = None
        expected_level = 20
        expected_colorization = None
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)
        assert issubclass(type(handler.stream), Stream)

    def test_init_stream_invalid(self):
        """Test if init raises TypeError when invalid stream is provided."""
        with self.assertRaises(TypeError):
            StreamHandler(stream=100)

    def test_stream_property_valid(self):
        """Test if stream property returns expected value."""
        handler = StreamHandler()
        stream = StderrStream()
        handler.stream = stream
        assert issubclass(type(handler.stream), Stream)

    def test_stream_property_invalid(self):
        """Test is stream property raises TypeError when invalid value is provided."""
        handler = StreamHandler()
        stream = 10
        with self.assertRaises(TypeError):
            handler.stream = stream

    def test_close(self):
        """Test close method"""
        handler = StreamHandler()
        handler.close()

    def test_emit_valid_no_colorization(self):
        """Test if emit method prints message as expected."""
        stream = StderrStream()
        handler = StreamHandler(stream=stream)
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
        expected_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test message\n'
        )
        self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_emit_valid_colorization(self):
        """Test if emit method prints message as expected."""
        stream = StderrStream()
        handler = StreamHandler(stream=stream)
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
        expected_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
        )
        self.assertIn(expected_output, repr(output_buffer.getvalue()))

    def test_emit_valid_colorization_no_display(self):
        """Test if emit method prints message as expected."""
        stream = StderrStream()
        handler = StreamHandler(stream=stream)
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

    def test_emit_invalid(self):
        """Test if emit method raises TypeError when invalid inputs are provided."""
        handler = StreamHandler()
        record = 100
        with self.assertRaises(TypeError):
            handler.emit(record, 100)

    def test_flush(self):
        """Test flush method."""
        handler = StreamHandler()
        handler.flush()


if __name__ == "__main__":
    unittest.main()
