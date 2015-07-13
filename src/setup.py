"""
setup.py
@author: franblas
@url: https://github.com/franblas/pyAPI
"""

from setuptools import setup, find_packages

setup(
    name='pyAPI',
    version='0.0.1',
    description='Data from multiple APIs with python',
    url='https://github.com/franblas/pyAPI',
    author='Francois Blas',
    author_email='francois_blas@hotmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Datascience :: Get Datas :: APIs',
        'License :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='api data development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['requests', 'colorama'],
)
