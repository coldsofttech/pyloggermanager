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
    "Handler",
    "ConsoleHandler",
    "FileHandler",
    "StreamHandler",
    "StderrHandler"
]
__name__ = "pyloggermanager.handlers"
__description__ = """
The pyloggermanager.handlers package provides classes responsible for handling log records
generated within the logger manager framework. It includes various handlers for processing log
messages, directing them to different destinations, and performing actions based on logging levels.

Below listed handler classes offer flexibility and customization options for managing log records
within the logger manager framework. They enable users to define how log messages are processed,
where they are directed, and how they are formatted, catering to various logging scenarios and
deployment environments.

Overall, the pyloggermanager.handlers package enhances the functionality of the logger manager
framework by providing a robust set of handlers for managing log records effectively and efficiently.
Users can choose and configure handlers based on their specific logging needs and infrastructure requirements.
"""

from pyloggermanager.handlers.__main__ import Handler, ConsoleHandler, FileHandler, StreamHandler, StderrHandler
