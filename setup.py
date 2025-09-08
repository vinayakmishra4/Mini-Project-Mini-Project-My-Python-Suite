from setuptools import setup, find_packages
import os

# Read the README file
with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="my_python_suite",  # Package name
    version="0.1.0",         # Version
    packages=find_packages(),
    install_requires=[],     # List dependencies here
    author="Vinayak Mishra",
    author_email="vmaugust24@gmail.com",
    description="A suite of Python utilities for everyday computing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vinayakmishra4/Project-My-Python-Suite",
    entry_points={
        "console_scripts": [
            "python-suite=python_suite.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires='>=3.7',
)