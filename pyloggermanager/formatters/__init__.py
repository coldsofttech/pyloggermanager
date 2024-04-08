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
    "DEFAULT_FORMAT",
    "CSV_FORMAT",
    "JSON_FORMAT",
    "DATE_FORMAT",
    "Formatter",
    "DefaultFormatter",
    "CSVFormatter",
    "JSONFormatter"
]
__name__ = "pyloggermanager.formatters"
__description__ = """
The pyloggermanager.formatters package provides classes for formatting log messages in various
formats within the logger manager framework. It includes implementations for formatting log messages
as CSV (Comma-Separated Values), JSON (JavaScript Object Notation), and the default text format.

Below listed formatter classes enable users to customize the appearance and structure of log messages
according to their requirements. By supporting different formats such as CSV and JSON, users have the
flexibility to choose the most suitable format for their logging needs, whether it's for human-readable
output, structured data storage, or integration with external systems.

Overall, the pyloggermanager.formatters package enhances the logger manager framework by offering
versatile formatting options for log messages, catering to a wide range of logging use cases and
preferences.
"""

from pyloggermanager.formatters.__main__ import DEFAULT_FORMAT, CSV_FORMAT, JSON_FORMAT, DATE_FORMAT, Formatter, \
    DefaultFormatter, CSVFormatter, JSONFormatter
