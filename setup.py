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
