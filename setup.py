from setuptools import setup, find_packages
from codecs import open
from os import path 

import uoi

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-uoi',
    version=uoi.__version__,
    packages=find_packages(),
    author='Gaetan Trellu - goldyfruit',
    author_email='gaetan.trellu@incloudus.com',
    description='Unified OpenStack Installer',
    long_description=long_description,
    include_package_data=True,
    url='https://www.uoi.io',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    license='Apache',
    keywords='Unified OpenStack Installer',
    install_requires=['sqlalchemy'],

)
