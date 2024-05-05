import inspect
import json
import unittest

from pycolorecho import ColorMapper, TextColor

from pyloggermanager import CallerFrame, Record
from pyloggermanager.formatters import Formatter, JSONFormatter
from pyloggermanager.handlers import Handler


class TestHandler(unittest.TestCase):
    """Unit test cases for Handler class."""

    def tearDown(self) -> None:
        handlers = Handler.get_handlers()
        for handler in handlers:
            handler.close()

    def test_init_no_input(self):
        """Test if init method is initialized without inputs."""
        handler = Handler()
        expected_name = None
        expected_level = 20
        expected_colorization = None
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_name_valid(self):
        """Test if init method is initialized with valid name input."""
        handler = Handler(name='TestHandler')
        expected_name = 'TestHandler'
        expected_level = 20
        expected_colorization = None
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_name_invalid(self):
        """Test if init raises TypeError when invalid name is provided."""
        with self.assertRaises(TypeError):
            Handler(name=100)

    def test_init_level_valid(self):
        """Test if init method is initialized with valid level."""
        handler = Handler(level=30)
        expected_name = None
        expected_level = 30
        expected_colorization = None
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_level_invalid(self):
        """Test if init raises TypeError when invalid level is provided."""
        with self.assertRaises(TypeError):
            Handler(level='test')

    def test_init_level_not_exist(self):
        """Test if init raises ValueError when level that do not exist."""
        with self.assertRaises(ValueError):
            Handler(level=100)

    def test_init_colorization_valid(self):
        """Test if init method is initialized with valid colorization."""
        colorization = ColorMapper()
        colorization.add_mapping('error', ['error'], text_color=TextColor.RED)
        handler = Handler(colorization=colorization)
        expected_name = None
        expected_level = 20
        expected_colorization = colorization
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_colorization_invalid(self):
        """Test if init raises TypeError when invalid colorization is provided."""
        with self.assertRaises(TypeError):
            Handler(colorization=100)

    def test_init_formatter_valid(self):
        """Test if init method is initialized with valid formatter."""
        formatter = JSONFormatter()
        handler = Handler(formatter=formatter)
        expected_name = None
        expected_level = 20
        expected_colorization = None
        self.assertEqual(handler.name, expected_name)
        self.assertEqual(handler.level, expected_level)
        self.assertEqual(handler.colorization, expected_colorization)
        assert issubclass(type(handler.formatter), Formatter)

    def test_init_formatter_invalid(self):
        """Test if init raises TypeError when invalid formatter is provided."""
        with self.assertRaises(TypeError):
            Handler(formatter=100)

    def test_colorization_property_valid(self):
        """Test if colorization property returns expected value."""
        handler = Handler()
        colorization = ColorMapper()
        colorization.add_mapping('error', ['error'], text_color=TextColor.RED)
        handler.colorization = colorization
        self.assertEqual(handler.colorization, colorization)

    def test_colorization_property_invalid(self):
        """Test if colorization property raises TypeError when invalid value is provided."""
        handler = Handler()
        colorization = 100
        with self.assertRaises(TypeError):
            handler.colorization = colorization

    def test_formatter_property_valid(self):
        """Test if formatter property returns expected value."""
        handler = Handler()
        formatter = JSONFormatter()
        handler.formatter = formatter
        assert issubclass(type(handler.formatter), Formatter)

    def test_formatter_property_invalid(self):
        """Test is formatter property raises TypeError when invalid value is provided."""
        handler = Handler()
        formatter = 10
        with self.assertRaises(TypeError):
            handler.formatter = formatter

    def test_level_property_valid(self):
        """Test if level property returns expected value."""
        level = 30
        handler = Handler()
        handler.level = level
        self.assertEqual(handler.level, level)

    def test_level_property_invalid(self):
        """Test if level property raises TypeError when invalid value is provided."""
        level = 'test'
        handler = Handler()
        with self.assertRaises(TypeError):
            handler.level = level

    def test_level_property_invalid_not_exist(self):
        """Test if level property raises ValueError when level which do not exist is provided."""
        level = 100
        handler = Handler()
        with self.assertRaises(ValueError):
            handler.level = level

    def test_name_property_valid(self):
        """Test if name property returns expected value."""
        name = 'TestHandler'
        handler = Handler()
        handler.name = name
        self.assertEqual(handler.name, name)

    def test_name_property_invalid(self):
        """Test if name property raises TypeError when invalid value is provided."""
        name = 100
        handler = Handler()
        with self.assertRaises(TypeError):
            handler.name = name

    def test_close(self):
        """Test close method"""
        handler = Handler()
        handler.close()

    def test_emit(self):
        """Test if emit method raises NotImplementedError."""
        handler = Handler()
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        with self.assertRaises(NotImplementedError):
            handler.emit(record, False)

    def test_format_valid(self):
        """Test if format method returns value as expected."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = JSONFormatter()
        handler = Handler()
        handler.formatter = formatter
        expected_output = {
            'time': f'{formatter.format_time(record.time.timetuple(), formatter.date_format)}',
            'levelName': 'WARNING',
            'message': 'Test message'
        }
        expected_output_json_str = json.dumps(expected_output, indent=4)
        self.assertEqual(handler.format(record), expected_output_json_str)

    def test_format_invalid(self):
        """Test if format method raises TypeError when invalid inputs are provided."""
        record = 100
        formatter = JSONFormatter()
        handler = Handler()
        handler.formatter = formatter
        with self.assertRaises(TypeError):
            handler.format(record)

    def test_flush(self):
        """Test if flush method raises NotImplementedError."""
        handler = Handler()
        with self.assertRaises(NotImplementedError):
            handler.flush()

    def test_get_handlers_none(self):
        """Test if the get handlers returns empty when no handlers are added."""
        assert len(Handler.get_handlers()) == 0

    def test_get_handlers_valid(self):
        """Test if the get handlers returns expected values."""
        Handler()
        assert len(Handler.get_handlers()) > 0

    def test_handle_valid(self):
        """Test if handle method raises NotImplementedError when valid values are provided."""
        caller_frame = CallerFrame().get_caller_details(inspect.currentframe())
        record = Record(
            message='Test message',
            logger_name='TestLogger',
            level_number=30,
            caller_frame=caller_frame
        )
        formatter = JSONFormatter()
        handler = Handler()
        handler.formatter = formatter
        with self.assertRaises(NotImplementedError):
            handler.handle(record, False)

    def test_handle_invalid(self):
        """Test if handle method raises TypeError when invalid inputs are provided."""
        record = 100
        formatter = JSONFormatter()
        handler = Handler()
        handler.formatter = formatter
        with self.assertRaises(TypeError):
            handler.handle(record, False)


if __name__ == "__main__":
    unittest.main()
