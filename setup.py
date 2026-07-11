from setuptools import setup, find_packages
import os

# Read the contents of your README file for the long_description
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="text-advanced",                     # The name people will use to pip install your library
    version="0.1.6",                       # The initial version of your package
    author="Monil Darediya",
    author_email="monildarediya1@gmail.com",
    description="A python library for advanced text management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Automatically find your package folders (like my_library/)
    packages=find_packages(), 
    
    # Supported Python versions
    python_requires=">=3.8", 
    
    # Third-party dependencies your library needs to run
    install_requires=[],
    
    # Metadata classifications for PyPI sorting
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
