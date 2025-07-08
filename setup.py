from setuptools import setup, find_packages

setup(
    name="PyUIRender",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="Qt UI file conversion tool",
    author="Istiak Noor Rabbi",
    author_email="istiaknoor26@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["PySide6"],
    entry_points={
        'console_scripts': ['pyuirender=PyUIRender.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",  # Add SPDX license identifier
    python_requires=">=3.7",
)