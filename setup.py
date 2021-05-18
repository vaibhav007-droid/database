# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in database/__init__.py
from database import __version__ as version

setup(
	name='database',
	version=version,
	description='Fetch Database',
	author='Vaibhav Parmar',
	author_email='parmarvaibhav773@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
