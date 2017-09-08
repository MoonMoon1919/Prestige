""" Setup script for PyPI """
import os
from setuptools import setup
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

setup(
    name='prestige',
    version='0.1',
    license='Apache License, Version 2.0',
    description='CLI tool for uploading images to s3',
    author="Max Moon, Perilune Industries",
    author_email='moon.maxwell@gmail.com',
    keywords="aws amazon web services s3 photo upload",
    platforms=['Any'],
    packages=['prestige'],
    entry_points = {
        'console_scripts': [
            'prestige=prestige.prestige:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)