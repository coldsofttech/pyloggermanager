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
