from setuptools import setup, find_packages

setup(
    name='mhw-api-wrapper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)