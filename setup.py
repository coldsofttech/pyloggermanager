# MIT License
#
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

from setuptools import setup

import pyloggermanager

setup(
    name=pyloggermanager.__name__,
    version=pyloggermanager.__version__,
    packages=[
        pyloggermanager.__name__,
        pyloggermanager.formatters.__name__,
        pyloggermanager.textstyles.__name__,
        pyloggermanager.handlers.__name__,
        pyloggermanager.streams.__name__
    ],
    url='https://github.com/coldsofttech/pyloggermanager',
    license='MIT',
    author='coldsofttech',
    description=pyloggermanager.__description__,
    requires_python=">=3.10",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=["logger", "logging", "logging-framework", "logger-manager"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)
