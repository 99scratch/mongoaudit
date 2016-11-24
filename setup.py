# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='IsMyMongoExposed',
    version='0.0.1',
    description='MongoDB security check',
    long_description=readme,
    author='Stampery Inc',
    author_email='info@stampery.com',
    url='https://github.com/stampery/ismymongoexposed',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
