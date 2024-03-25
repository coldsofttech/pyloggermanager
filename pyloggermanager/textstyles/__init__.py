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
    "TextBackgroundColor",
    "TextColor",
    "TextEffect"
]
__name__ = "pyloggermanager.textstyles"
__description__ = """
The pyloggermanager.textstyles package provides utilities for defining and applying text styles
to log messages within the logger manager framework. It includes classes for specifying text 
colors, background colors, and text effects, allowing users to customize the appearance of log 
messages according to their preferences.

This package is designed to enhance the visual representation of log messages by providing a 
flexible and intuitive way to apply various text styles. By incorporating these text styles 
into log messages, users can improve readability, emphasize important information, and differentiate
between different types of log entries.

Overall, the pyloggermanager.textstyles package complements the logger manager framework by 
offering tools for creating visually appealing and informative log messages, contributing to a 
more effective logging experience.
"""

from pyloggermanager.textstyles.__main__ import TextBackgroundColor, TextColor, TextEffect
