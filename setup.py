#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-disqus2',
    version='0.4.4',
    description='Export comments and integrate DISQUS into your Django website',
    author='Wojciech Nowak',
    author_email='vojtek.nowak@gmail.com',
    url='https://github.com/YoungCoder/django-disqus',
    license='New BSD License',
    classifiers=[
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
    ],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)
