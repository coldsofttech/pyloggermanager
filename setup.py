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
    description=pyloggermanager.__description__
)
