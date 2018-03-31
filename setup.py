#!/usr/bin/env python
import nfccli
from setuptools import setup

extras = {
    'nfccli': [
        'docopt',
        'python-dotenv',
        'pyscard',
        'raven',
    ],
    'tests': [
        'pytest',
        'pytest-cov',
        'pytest-dotenv',
    ],
}

extras['dev'] = list(reduce(lambda x, y: x + y, extras.values()))

setup(
    author='Pablo Escodebar',
    author_email='escodebar@gmail.com',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 2.7',
    ],
    description='Read and write nfc tags through the command line interface',
    entry_points={
        'console_scripts': [
            'nfccli = nfccli.cli:run',
        ],
    },
    extras_require=extras,
    install_requires=extras['nfccli'],
    license='Affero GPL',
    maintainer='Pablo Escodebar',
    maintainer_email='escodebar@gmail.com',
    name='nfccli',
    packages=['nfccli'],
    python_requires='>=2.7.*, <3',
    setup_requires=['pytest-runner'],
    tests_require=extras['tests'],
    version=nfccli.__version__,
)
