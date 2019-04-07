#!/usr/bin/env python3
from setuptools import find_packages, setup

# with open('README.rst') as f:
#     readme = f.read()

install_requires=[
    'Flask',
    'Flask_RESTful',
    'PyYAML',
]

tests_requires=[
    'pytest',
    'pytest-cov',
]

setup(
    name='pgapi_backup',
    version='0.0.1',
    license='MIT',
    author='Julian Schauder',
    author_email='julian.schauder@credativ.de',
    description='Backup-Plugin for a simple REST API for postgresql on Debian systems.',
    # long_description=readme,
    packages=['pgapi_backup'],
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_requires=tests_requires,
    #entry_points={
    #     'console_scripts': [
    #         'pgapi = pgapi.api:main',
    #     ],
    # },
)
