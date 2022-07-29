from ec2price import __author__, __author_email__, __version__
from setuptools import setup

setup(name='ec2price',
      version=__version__,
      description="AWS EC2 Pricing Tool.",
      url="https://github.com/anubhavmishra/ec2price",
      author=__author__,
      author_email=__author_email__,
      scripts=['ec2price'],
      )