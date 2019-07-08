from setuptools import setup

setup(name='pyqmlativ',
      version='0.1',
      description="A library for accessing Skyward QMLATIV's generic API.",
      url='https://github.com/samterfa/pyqmlativ',
      author='Sam Terfa',
      author_email='samterfa@gmail.com',
      license='MIT',
      packages=['pyqmlativ'],
      install_requires=[
            'json',
            'pandas',
            'os',
            'requests',
            'requests_oauthlib',
      ],
      zip_safe=False)
