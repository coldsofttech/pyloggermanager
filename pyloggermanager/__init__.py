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
    "CallerFrame",
    "Colorization",
    "FileMode",
    "Lock",
    "LogLevel",
    "Record",
    "Logger",
    "Manager",
    "Registry",
    "RootLogger",
    "load_config",
    "get_logger",
    "critical",
    "debug",
    "error",
    "info",
    "warning",
    "log",
    "disable",
    "shutdown",
    "formatters",
    "handlers",
    "streams",
    "textstyles",
    "__author__",
    "__description__",
    "__name__",
    "__version__"
]
__author__ = "coldsofttech"
__description__ = """
The pyloggermanager package is a vital logging framework for Python applications, providing developers with essential
tools to streamline logging operations. Its primary function is to simplify the recording and organization of log
messages, including critical information, debugging messages, errors, and warnings. By offering a centralized interface
and robust functionalities, the package facilitates efficient monitoring and troubleshooting processes.

With its intuitive interface, the pyloggermanager package enables developers to seamlessly integrate logging mechanisms
into their applications. This allows for systematic recording and categorization of log entries based on severity
levels, enhancing readability and prioritization of issues. Moreover, the package offers flexibility in customizing
logging configurations to suit specific project requirements, including formatting, output destinations, and thread
safety.

Beyond technical capabilities, the pyloggermanager package contributes to the reliability and maintainability of Python
applications. It establishes consistent logging practices, simplifying collaboration, code reviews, and issue
resolution across development teams. Overall, the pyloggermanager package is an invaluable asset for developers aiming
to implement robust logging solutions, ensuring efficient and resilient application performance.
"""
__name__ = "pyloggermanager"
__version__ = "0.1.1"

from pyloggermanager import formatters
from pyloggermanager import handlers
from pyloggermanager import streams
from pyloggermanager import textstyles
from pyloggermanager.__main__ import CallerFrame, Colorization, FileMode, Lock, LogLevel, Record, Logger, Manager, \
    Registry, RootLogger, load_config, get_logger, critical, debug, error, info, warning, log, disable, shutdown
