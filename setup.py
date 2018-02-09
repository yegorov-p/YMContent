from setuptools import setup, find_packages
import sys, os
from YMContent import constants


setup(name='YMContent',
      version=constants.VERSION,
      description="Yandex.Market Content API SDK",
      long_description="""\
Yandex.Market Content API SDK""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='yandex market',
      author='Pavel Yegorov',
      author_email='yegorov.p@gmail.com',
      url='https://github.com/yegorov-p/YMContent',
      license='',
      packages=['YMContent'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['requests'],
      )
