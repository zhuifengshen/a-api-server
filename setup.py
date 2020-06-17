#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import io
import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command

about = {}
here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'a_api_server', '__about__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

install_requires = ["flask"]


class PypiUploadCommand(Command):
    """ Build and publish this package and make a tag.
        Support: python setup.py pypi
        Copied from requests_html
    """
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in green color."""
        print('\033[0;32m{0}\033[0m'.format(s))

    def initialize_options(self):
        """ override
        """
        pass

    def finalize_options(self):
        """ override
        """
        pass

    def run(self):
        self.status('Building Source and Wheel (universal) distribution...')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine...')
        os.system('twine upload dist/*')

        self.status('Publishing git tags...')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        try:
            self.status('Removing current build artifacts...')
            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'build'))
            rmtree(os.path.join(here, 'a_api_server.egg-info'))  # custom
        except OSError:
            pass

        self.status('Congratulations! Upload PyPi and publish git tag successfully...')
        sys.exit()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=about['__keywords__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=find_packages(exclude=['tests', 'test.*', 'docs']),  # custom
    package_data={  # custom
        '': ['README.md']
    },
    install_requires=install_requires,
    extras_require={},
    python_requires='>=2.7, <4',  # custom
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # custom
        'console_scripts': [
            'a_api_server=a_api_server.api_server:cli_main',
        ]
    },
    cmdclass={
        # python3 setup.py pypi
        'pypi': PypiUploadCommand
    }
)