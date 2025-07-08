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

Versioning:
    Uses versioneer for automatic version management
"""

import os
from . import _version
from ._version import get_versions


__author__ = "Istiak Noor Rabbi"
__email__ = "istiaknoor26@gmail.com"
__description__ = "A tool for converting Qt .ui files to Python code"
__license__ = "MIT"


__version__ = get_versions()['version']
del get_versions


from . import _version
__version__ = _version.get_versions()['version']


from .appWindow import Ui_AppMainWindow
from .success_dia import Ui_success_dialog
from .failed_dia import Ui_fail_dialog
from .resources_rc import *


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

# Versioneer configuration
def get_cmdclass():

    from versioneer import get_cmdclass as _get_cmdclass
    return _get_cmdclass()

def get_version():

    return __version__


del _version