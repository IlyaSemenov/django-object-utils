# coding=utf-8
from distutils.core import setup
from setuptools import setup, find_packages

"""
Update Django model objects without race conditions
"""

setup(
	name='django-object-utils',
	version='0.0.1',
	url='https://github.com/IlyaSemenov/django-object-utils',
	license='BSD',
	author='Ilya Semenov',
	author_email='ilya@semenov.co',
	description=__doc__,
	long_description=open('README.rst').read(),
	packages=['django_object_utils'],
	install_requires=['Django>=1.4'],
	classifiers=[],
)
