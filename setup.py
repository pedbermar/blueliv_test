# from setuptools import setup, find_packages
from distutils.core import setup

setup(name='blueliv_test',
      version='0.1',
      description='Bluelib test crawler and API',
      url='http://github.com/pedbermar/blueliv_test',
      author='Pedro Berrocal',
      packages=['blueliv_test', 'blueliv_test.crawler', 'blueliv_test.api'],
      author_email='pedbermar@gmail.com',
      license='MIT'
)
