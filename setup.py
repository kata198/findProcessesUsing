#!/usr/bin/env python

from setuptools import setup



if __name__ == '__main__':

    try:
        with open('README.rst', 'r') as f:
            long_description = f.read()
    except:
        long_description = ''

    setup(name='findProcessesUsing',
            version='2.1.1',
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            scripts=['findProcessesUsing'],
            install_requires=['ProcessMappingScanner>1.0'],
            url='https://github.com/kata198/findProcessesUsing',
            maintainer_email='kata198@gmail.com',
            description='Application which scans running processes on the system for given mappings (shared libraries, executables) or open file descriptors',
            long_description=long_description,
            license='LGPLv3',
            keywords=['find', 'process', 'using', 'file', 'files', 'so', 'mapping', 'scanner', 'unix', 'proc', 'mappings', 'lib', 'detect', 'executable', 'shared', 'object'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
            ]
    )



