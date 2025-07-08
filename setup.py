#!/usr/bin/env python
import re
import os
import codecs
from setuptools import setup, find_packages

# Read version from package file
def get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, "PyUIRender", "version.py")
    with codecs.open(version_file, "r") as f:
        return re.search(r"__version__ = \"(.+?)\"", f.read()).group(1)

# Get long description from README
def get_long_description():
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, "README.md"), "r", "utf-8") as f:
        return f.read()

setup(
    name="PyUIRender",
    version=get_version(),
    description="Qt UI file conversion tool",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/PyUIRender",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PySide6>=6.4.0",
    ],
    entry_points={
        'console_scripts': [
            'pyuirender=PyUIRender.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    license="MIT",
)