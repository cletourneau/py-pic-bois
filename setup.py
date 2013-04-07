import sys

from setuptools import setup

from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox

        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='picbois',
    install_requires=[
        'requests',
        'flask',
        'gunicorn',
    ],
    # packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    # entry_points={'console_scripts': [
    #     'picbois=pyweb.main:run',
    #     ]},
    # package_data={
    #     'picbois': [
    #         'resources/config/*.cfg',
    #         'resources/init-script',
    #         'salesforce/resources/*.wsdl',
    #         ],
    # },
    cmdclass={'test': Tox},
)
