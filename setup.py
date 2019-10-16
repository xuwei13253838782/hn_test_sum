#from distutils.core import setup
from setuptools import setup, find_packages

# http://guide.python-distribute.org/quickstart.html
# python setup.py sdist
# python setup.py register
# python setup.py sdist upload
# pip install django-dynamic-fixture
# pip install django-dynamic-fixture --upgrade --no-deps
# Manual upload to PypI
# http://pypi.python.org/pypi/django-smart-autoregister
# Go to 'edit' link
# Update version and save
# Go to 'files' link and upload the file

VERSION = '0.0.1'

tests_require = []

install_requires = []

setup(name='hn_test_sum',
      url='https://github.com/xuwei13253838782/hn_test_sum',
      author="wei.xu",
      author_email='143482020@qq.com',
      keywords='python django admin autoregister',
      description='Automatically register models in the admin interface in a smart way.',
      license='MIT',
      classifiers=[
          'Operating System :: OS Independent',
          'Topic :: Software Development',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],

      version=VERSION,
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='runtests.runtests',
      extras_require={'test': tests_require},

      entry_points={ 'nose.plugins': [] },
      packages=find_packages(),
)
