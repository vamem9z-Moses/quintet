#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):

    # long option, short option, description
    user_options = [
                    ('flakes', None, 'Use pyflakes'),
                    ('coverage', 'C', 'Show coverage statistics'),
                    ('jenkins', None, 'Options for jenkins'),

     ]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.flakes = False
        self.coverage = False
        self.jenkins = False
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['quintet/tests']
        if self.flakes:
            self.test_args.append('--flakes')
        if self.coverage:
            self.test_args += [ '--cov', 'quintet', '--cov-report', 'term-missing']
        if self.jenkins:
            self.test_args += [ '--cov', 'quintet', '--cov-report', 'xml', 'term-missing' ]
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='Quintet',
      version='0.1',
      description='Quintet Framework',
      author='Moses E. Miles III',
      author_email='vamem9z@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license = 'MIT',
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
      ],
      install_requires=['docker-py==0.2.3'],
      tests_require=['pytest==2.5.2',
                     'pytest-flakes',
                     'pytest-cov==1.6'],
      cmdclass = {'test':PyTest},
    )


