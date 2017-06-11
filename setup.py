#!/usr/bin/env python

from setuptools import setup



if __name__ == '__main__':

    summary = 'Application which scans running processes on the system for given mappings (shared libraries, executables) or open file descriptors'
    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except Exception as e:
        sys.stderr.write('Exception reading long description: %s\n' %(str(e),))
        long_description = summary

    setup(name='findProcessesUsing',
            version='2.3.0',
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            scripts=['findProcessesUsing'],
            install_requires=['ProcessMappingScanner>=2.2.2'],
            requires=['ProcessMappingScanner'],
            url='https://github.com/kata198/findProcessesUsing',
            maintainer_email='kata198@gmail.com',
            description=summary,
            long_description=long_description,
            license='LGPLv3',
            keywords=['find', 'process', 'using', 'file', 'files', 'so', 'mapping', 'scanner', 'unix', 'proc', 'mappings', 'lib', 'detect', 'executable', 'shared', 'object', 'cwd'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
                          'Programming Language :: Python :: 3.5',
                          'Programming Language :: Python :: 3.6',
            ]
    )



