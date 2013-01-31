#!/usr/bin/env python

from setuptools import setup


setup(
    name='parawrap',
    version='1.0',
    description='Paragraph wrapping and filling.',
    long_description=open('README.rst').read(),
    license='Apache Software License, version 2.0',

    author='Ecometrica',
    author_email='admin@ecometrica.com',
    url='https://github.com/ecometrica/parawrap',

    py_modules=['parawrap'],
    include_package_data=True,

    test_suite='tests',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Filters',
    ],

    zip_safe=True,
)
