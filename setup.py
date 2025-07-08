#!/usr/bin/env python
import versioneer
from setuptools import setup, find_packages

setup(
    name="PyUIRender",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Qt UI file conversion tool",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PySide6",
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
)