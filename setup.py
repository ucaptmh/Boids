#!/usr/bin/env python
__author__ = 'third'
from setuptools import setup, find_packages
setup(
    name = "Boids",
    version ="0.1.0",
    description='Programme to simulate the flocking behaviour of birds',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/boids'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/ucaptmh/Boids',
    keywords='simulation flocking boids',
    author='Thomas Hird',
    author_email='thomas.hird.16@ucl.ac.uk',
    license='MIT',
    entry_points=dict(console_scripts=[
        'boids = boids.__main__:process']),
    install_requires = ['argparse', 'matplotlib', 'numpy']
)