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

import io
import sys
import unittest

from pyloggermanager.streams import StderrStream


class TestStderrStream(unittest.TestCase):
    """Unit test cases for StderrStream class"""

    def test_write_invalid(self):
        """
        Test if TypeError is raised when invalid datatype is passed.
        """
        stderr_stream = StderrStream()
        with self.assertRaises(TypeError):
            stderr_stream.write({'test'})

    def test_write_valid(self):
        """
        Test if message is written to stderr.
        """
        stderr_stream = StderrStream()
        message = 'Test message'

        output_buffer = io.StringIO()
        sys.stderr = output_buffer
        stderr_stream.write(message)
        sys.stderr = sys.__stderr__

        self.assertEqual(output_buffer.getvalue(), message)

    def test_flush(self):
        """
        Test if flush clears stdout.
        """
        stderr_stream = StderrStream()

        output_buffer = io.StringIO()
        sys.stderr = output_buffer
        stderr_stream.flush()
        sys.stderr = sys.__stderr__

        self.assertEqual(output_buffer.getvalue(), '')


if __name__ == "__main__":
    unittest.main()
