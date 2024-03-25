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


class Stream:
    """
    Abstract base class representing an output stream.
    Defines two abstract methods: 'write()' and 'flush()', which must be implemented
    by subclasses.
    """

    def write(self, message: str) -> None:
        """
        Abstract method to write the given message to the stream.
        Subclasses must implement this method.

        :param message: The message to be written to the stream.
        :type message: str
        :return: None
        """
        raise NotImplementedError('write() method must be implemented in subclasses.')

    def flush(self) -> None:
        """
        Abstract method to flush the stream, ensuring all buffered data is written.
        Subclasses must implement this method.

        :return: None
        """
        raise NotImplementedError('flush() method must be implemented in subclasses.')


class StdoutStream(Stream):
    """
    A stream that writes messages to the standard output (sys.stdout).
    Inherits from the 'Stream' class and overrides the 'write' and 'flush' methods.
    """

    def write(self, message: str) -> None:
        """
        Writes the given message to the standard output (sys.stdout).

        :param message: The message to be written.
        :type message: str
        :return: None
        """
        if not isinstance(message, str):
            raise TypeError('message should be a string.')

        sys.stdout.write(message)

    def flush(self) -> None:
        """
        Flushes the output buffer of the standard output (sys.stdout),
        ensuring all buffered data is written.

        :return: None
        """
        sys.stdout.flush()


class StderrStream(Stream):
    """
    A stream for writing messages to the standard error (sys.stderr) output.
    Overrides the 'write' method to write messages to sys.stderr and the 'flush' method
    to flush the sys.stderr buffer.
    """

    def write(self, message: str) -> None:
        """
        Writes the provided message to the standard error (sys.stderr) output.

        :param message: Message to be written to stderr.
        :type message: str
        :return: None
        """
        if not isinstance(message, str):
            raise TypeError('message should be a string.')

        sys.stderr.write(message)

    def flush(self) -> None:
        """
        Flushes the standard error (sys.stderr) buffer.

        :return: None
        """
        sys.stderr.flush()


class TerminalStream(Stream):
    """
    A stream for writing messages to the terminal.
    Inherits from the 'Stream' class and overrides the 'write' and 'flush' methods.
    """

    def write(self, message: str) -> None:
        """
        Writes the provided message to the terminal.

        :param message: The message to be written.
        :type message: str
        :return: None
        """
        if not isinstance(message, str):
            raise TypeError('message should be a string.')

        print(message, end='')

    def flush(self) -> None:
        """
        Flushes the output buffer, but does nothing for the terminal stream since output is
        immediately displayed.

        :return: None
        """
        pass
