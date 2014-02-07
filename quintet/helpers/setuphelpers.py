
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):

    # long option, short option, description
    user_options = [
                    ('flakes', None, 'Use pyflakes'),
                    ('coverage', 'C', 'Show coverage statistics'),
                    ('jenkins', None, 'Test setup for jenkins'),
     ]
    def add_project_specific_options(self):
        """
            Placeholder for project specific options

            This will allow the subclass to add project specific options
        """
        pass

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.flakes = False
        self.coverage = False
        self.jenkins = False
        # package name to be tested
        self.package_name = False
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.add_project_specific_options()
        if self.flakes:
            self.test_args.append('--flakes')
        if self.coverage:
            self.test_args += [ '--cov', self.package_name, '--cov-report', 'term-missing']
        if self.jenkins:
            self.test_args += [ '--cov', self.package_name, '--cov-report', 'xml']
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)