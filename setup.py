import os
import re
from setuptools import setup, find_packages

# Get version from git using our helper script
def get_version():
    try:
        version_file = os.path.join(os.path.dirname(__file__), "PyUIRender", "get_version.py")
        with open(version_file, "r") as f:
            content = f.read()
        match = re.search(r'return "([^"]+)"', content)
        if match:
            return match.group(1)
    except FileNotFoundError:
        pass
    return "0.0.0.dev"

setup(
    name="PyUIRender",
    version=get_version(),
    description="Qt UI file conversion tool",
    author="Your Name",
    author_email="your.email@example.com",
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