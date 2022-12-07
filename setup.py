from setuptools import find_packages, setup


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='pgbackup',
    version='0.1.0',
    author='João Kiakumbo',
    description='A utility for backing up postgreSQL database.',
    long_description= long_description,
    url='https://github.com/JKiakumboS/pgbackup',
    packages=find_packages('src')
)