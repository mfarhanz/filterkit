from setuptools import find_packages, setup
from os import path

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='filterkit',
    packages=find_packages(include=['filterkit', 'filterkit.*']),
    version='0.1.3',
    description='A library with efficient implementations for various image processing methods.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Farhan Zia',
    url="https://github.com/mfarhanz/filterkit",
    install_requires=['pillow', 'numba'],
    tests_require=['pytest'],
    test_suite='tests',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
