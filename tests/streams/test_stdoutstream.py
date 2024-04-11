import io
import sys
import unittest

from pyloggermanager.streams import StdoutStream


class TestStdoutStream(unittest.TestCase):
    """Unit test cases for StdoutStream class"""

    def test_write_invalid(self):
        """
        Test if TypeError is raised when invalid datatype is passed.
        """
        stdout_stream = StdoutStream()
        with self.assertRaises(TypeError):
            stdout_stream.write({'test'})

    def test_write_valid(self):
        """
        Test if message is written to stdout.
        """
        stdout_stream = StdoutStream()
        message = 'Test message'

        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        stdout_stream.write(message)
        sys.stdout = sys.__stdout__

        self.assertEqual(output_buffer.getvalue(), message)

    def test_flush(self):
        """
        Test if flush clears stdout.
        """
        stdout_stream = StdoutStream()

        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        stdout_stream.flush()
        sys.stdout = sys.__stdout__

        self.assertEqual(output_buffer.getvalue(), '')


if __name__ == "__main__":
    unittest.main()
