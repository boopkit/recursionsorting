from setuptools import setup, find_packages

setup(
    name='recursionsorting',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/boopkit/recursionsorting',
    author='Tamanique Kampman',
    author_email='tamakampman@gmail.com'
)
