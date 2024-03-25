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
