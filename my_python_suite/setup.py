from setuptools import setup, find_packages

setup(
    name="my_python_suite",  # Package name
    version="0.1.0",         # Version
    packages=find_packages(),
    install_requires=[],     # List dependencies here
    author="Vinayak Mishra",
    author_email="youremail@example.com",
    description="A suite of Python utilities for everyday computing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vinayakmishra4/Project-My-Python-Suite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)