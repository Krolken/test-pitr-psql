from setuptools import setup, find_packages

setup(
    name='test_pitr',
    version='1.0.0',
    url='test',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=['sqlalchemy'],
)