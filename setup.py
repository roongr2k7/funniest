from setuptools import setup

with open('requirement.txt', 'r') as f:
  lines = f.read().split('\n')

requirements = [package for package in lines if package and not package.startswith('#')]

setup(name='funniest',
      version='0.4',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      zip_safe=False,
      install_requires=requirements
      )
