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

# Package metadata
__author__ = "istiak Noor Rabbi"
__email__ = "istiaknoor@gmail.com.com"
__description__ = "A tool for converting Qt .ui files to Python code"
__license__ = "MIT"

# Import key components for easier access
from .appWindow import Ui_AppMainWindow
from .success_dia import Ui_success_dialog
from .failed_dia import Ui_fail_dialog
from .resources_rc import *

# Dynamic version import
try:
    from importlib.metadata import version, PackageNotFoundError
    __version__ = version("PyUIRender")
except (PackageNotFoundError, ImportError):
    # Fallback for development mode
    try:
        from setuptools_scm import get_version
        __version__ = get_version(root='..', relative_to=__file__)
    except (ImportError, LookupError):
        __version__ = "0.0.0.dev"

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