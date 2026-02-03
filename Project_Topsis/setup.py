from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Divyansh-102303964",            
    version="1.0.0",
    author="Divyansh Sharma",
    author_email="dsharma6_be23@thapar.edu",      
    description="A Python package for implementing TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis_divyansh_102303964.topsis:main', 
        ],
    },
)