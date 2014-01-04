#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='text_comparer',
        version='0.0.2',
        description='Metric for comparing text',
        keywords = '',
        url='https://github.com/sergeio/text_comparer',
        author='Sergei Orlov',
        author_email='',
        license='BSD',
        packages=['text_comparer'],
        install_requires=[''],
        test_suite='tests',
        long_description=read('README.md'),
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Programming Language :: Python',
        ],
    )

if __name__ == '__main__':
    run_setup()
