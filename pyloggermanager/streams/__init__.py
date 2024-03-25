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

__all__ = [
    "Stream",
    "StdoutStream",
    "StderrStream",
    "TerminalStream"
]
__name__ = "pyloggermanager.streams"
__description__ = """
The pyloggermanager.streams package provides classes related to handling output streams for log records
within the logger manager framework. These classes define different types of streams that log messages
can be directed to, allowing for flexible and customizable logging behaviour.

Below listed stream classes offer versatility in directing log messages to different output
channels, allowing users to customize logging behavior based on their application's requirements 
and environment configuration. By supporting various stream types, the logger manager framework 
enables users to control where log records are displayed or stored, facilitating effective logging 
and troubleshooting processes.

Overall, the pyloggermanager.streams package enhances the functionality of the logger manager framework 
by providing a range of stream classes for directing log messages to different output channels. Users can
leverage these classes to tailor their logging setup to suit their specific needs and preferences, ensuring 
efficient management and processing of log records.
"""

from pyloggermanager.streams.__main__ import Stream, StdoutStream, StderrStream, TerminalStream
