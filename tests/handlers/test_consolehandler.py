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
import io
import sys
import unittest

from pyloggermanager import CallerFrame, Record, Colorization
from pyloggermanager.formatters import Formatter
from pyloggermanager.handlers import ConsoleHandler, Handler
from pyloggermanager.streams import Stream, StdoutStream
from pyloggermanager.textstyles import TextColor


class TestConsoleHandler(unittest.TestCase):
    """Unit test cases for ConsoleHandler class."""

    def tearDown(self) -> None:
        handlers = Handler.get_handlers()
        for handler in handlers:
            handler.close()

    def test_init_no_input(self):
        """Test if init method is initialized without inputs."""
        handler = ConsoleHandler()
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
        stream = StdoutStream()
        handler = ConsoleHandler(stream=stream)
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
            ConsoleHandler(stream=100)

    def test_stream_property_valid(self):
        """Test if stream property returns expected value."""
        handler = ConsoleHandler()
        stream = StdoutStream()
        handler.stream = stream
        assert issubclass(type(handler.stream), Stream)

    def test_stream_property_invalid(self):
        """Test is stream property raises TypeError when invalid value is provided."""
        handler = ConsoleHandler()
        stream = 10
        with self.assertRaises(TypeError):
            handler.stream = stream

    def test_close(self):
        """Test close method"""
        handler = ConsoleHandler()
        handler.close()

    def test_emit_valid_no_colorization(self):
        """Test if emit method prints message as expected."""
        handler = ConsoleHandler()
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        handler.emit(record)
        sys.stdout = sys.__stdout__
        expected_output = (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test message'
        )
        self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_emit_valid_colorization(self):
        """Test if emit method prints message as expected."""
        handler = ConsoleHandler()
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test error message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        colorization = Colorization()
        colorization.set_keyword_color_mapping('error', ['error'], TextColor.RED)
        handler.colorization = colorization
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        handler.emit(record)
        sys.stdout = sys.__stdout__
        expected_output = (
            f'{TextColor.RED}'
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
            f'{Colorization.RESET}'
        ) if Colorization.is_colorization_supported() else (
            f'{handler.formatter.format_time(record.time.timetuple(), handler.formatter.date_format)}'
            f' :: WARNING :: Test error message'
        )
        self.assertEqual(repr(output_buffer.getvalue()), repr(expected_output))

    def test_emit_invalid(self):
        """Test if emit method raises TypeError when invalid inputs are provided."""
        handler = ConsoleHandler()
        record = 100
        with self.assertRaises(TypeError):
            handler.emit(record)

    def test_flush(self):
        """Test flush method."""
        handler = ConsoleHandler()
        handler.flush()


if __name__ == "__main__":
    unittest.main()
