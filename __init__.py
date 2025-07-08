"""
PyUIRender - A Qt UI File Conversion Tool

This package provides functionality to convert Qt Designer .ui files into
Python files compatible with PyQt5, PyQt6, or PySide6 frameworks.

Features:
- Convert single or multiple .ui files at once
- Support for PyQt5, PyQt6, and PySide6 output formats
- Save output directory preference
- Progress tracking and error handling

Modules:
    main: Main application entry point
    appWindow: Main window UI definition
    success_dia: Success dialog UI definition
    failed_dia: Failure dialog UI definition
    convert_pyqt5: PyQt5 conversion module
    convert_pyqt6: PyQt6 conversion module
    convert_pyside6: PySide6 conversion module
    resources_rc: Compiled resource file for application assets
"""

import os
import subprocess
import sys

# Package metadata
__author__ = "Your Name"
__email__ = "your.email@example.com"
__description__ = "A tool for converting Qt .ui files to Python code"
__license__ = "MIT"

# Version management
__version__ = "1.0.0"  # Default version

# Try to get version from git if available
try:
    # Get git describe output for version
    result = subprocess.run(
        ["git", "describe", "--tags", "--dirty", "--always"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
        cwd=os.path.dirname(__file__)
    )
    __version__ = result.stdout.strip()
except (subprocess.CalledProcessError, FileNotFoundError, OSError):
    # Fallback to default version
    pass

# Import key components for easier access
from .appWindow import Ui_AppMainWindow
from .success_dia import Ui_success_dialog
from .failed_dia import Ui_fail_dialog
from .resources_rc import *

# Package initialization message
print(f"Initializing PyUIRender v{__version__}")

def get_converters():
    """Return available conversion frameworks"""
    return ["PyQt5", "PyQt6", "PySide6"]

def about():
    """Return package information"""
    return (
        f"PyUIRender v{__version__}\n"
        f"Author: {__author__}\n"
        f"Email: {__email__}\n"
        f"License: {__license__}\n"
        f"Description: {__description__}"
    )

# Clean up namespace
del os, subprocess, sys