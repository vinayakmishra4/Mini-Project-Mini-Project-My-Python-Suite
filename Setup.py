# Directory structure:
# Project-My-Python-Suite/
# └─ mypythonsuite/
#    ├─ __init__.py (empty file)
#    ├─ PythonSuite.py  # (with main() already defined)
#    ├─ Calc.py
#    ├─ UnitConvert.py
#    └─ funfact.py
# setup.py in root, README.md in root

# setup.py content:
from setuptools import setup, find_packages

setup(
    name="mypythonsuite",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "pythonsuite = mypythonsuite.PythonSuite:main",
        ],
    },
    author="Vinayak Mishra",
    description="A beginner-friendly Python utility suite with calculator, unit converter, fun facts, and more.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vinayakmishra4/Project-My-Python-Suite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)