import sys
import unittest

from pyloggermanager.handlers import Handler, StderrHandler


class TestStderrHandler(unittest.TestCase):
    """Unit test cases for StderrHandler class."""

    def tearDown(self) -> None:
        handlers = Handler.get_handlers()
        for handler in handlers:
            handler.close()

    def test_init_no_input(self):
        """Test if init method is initialized without inputs."""
        handler = StderrHandler()
        expected_level = 30
        self.assertEqual(handler.level, expected_level)

    def test_stream_property(self):
        """Test if stream property returns expected value."""
        handler = StderrHandler()
        expected_stream = sys.stderr
        self.assertEqual(handler.stream, expected_stream)


if __name__ == "__main__":
    unittest.main()
