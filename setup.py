#!/usr/bin/env python

from setuptools import setup, find_packages
from quintet.helpers.setuphelpers import PyTest

class QuintetPyTest(PyTest):
    """
        Project specific test options for quintet
    """
    def add_project_specific_options(self):
        self.test_args = ['quintet/tests']
        self.package_name = 'quintet'

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
      cmdclass = {'test':QuintetPyTest},
    )


