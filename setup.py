from setuptools import setup
from YMContent import constants

setup(name='YMContent',
      version=constants.VERSION,
      description="Yandex.Market Content API SDK",
      long_description="""Yandex.Market Content API SDK""",
      classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries'],
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
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
