from setuptools import setup, find_packages
try:
    import md5  # fix for "No module named _md5" error
except ImportError:
    # python 3 moved md5
    from hashlib import md5

with open("README.rst") as f:
    long_description = f.read()


tests_require = [
    "dill",
    "coverage",
    "coveralls",
    "mock",
    "nose",
]

setup(name="expiringdict",
      version="2.0.0",
      description="Dictionary with auto-expiring values for caching purposes",
      long_description=long_description,
      author="Anton Efimenko",
      author_email="anton@mailgunhq.com",
      url="https://github.com/mailgun/expiringdict",
      license="Apache 2",
      packages=find_packages(exclude=["tests"]),
      include_package_data=True,
      zip_safe=True,
      tests_require=tests_require,
      install_requires=[
          "typing",
      ],
      extras_require={
          "tests": tests_require,
      })
