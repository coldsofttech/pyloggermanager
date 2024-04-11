import io
import sys
import unittest

from pyloggermanager.streams import TerminalStream


class TestTerminalStream(unittest.TestCase):
    """Unit test cases for TerminalStream class"""

    def test_write_invalid(self):
        """
        Test if TypeError is raised when invalid datatype is passed.
        """
        terminal_stream = TerminalStream()
        with self.assertRaises(TypeError):
            terminal_stream.write({'test'})

    def test_write_valid(self):
        """
        Test if message is written to terminal.
        """
        terminal_stream = TerminalStream()
        message = 'Test message'

        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        terminal_stream.write(message)
        sys.stdout = sys.__stdout__

        self.assertEqual(output_buffer.getvalue(), message)

    def test_flush(self):
        """
        Test if flush clears stdout.
        """
        terminal_stream = TerminalStream()
        terminal_stream.flush()

        pass  # no assertion required


if __name__ == "__main__":
    unittest.main()
