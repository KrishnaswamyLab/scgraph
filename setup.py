import os
import sys
from setuptools import setup, find_packages

install_requires = [
    'graphtools',
    'magic-impute',
    'phate',
    'meld',
]

if sys.version_info[:2] < (3, 5):
    raise RuntimeError("Python version >=3.5 required.")

version_py = os.path.join(os.path.dirname(
    __file__), 'scgraph', 'version.py')
version = open(version_py).read().strip().split(
    '=')[-1].replace('"', '').strip()

readme = open('README.md').read()

setup(name='scprep',
      version=version,
      description='scgraph',
      author='',
      author_email='',
      packages=find_packages(),
      license='MIT License',
      install_requires=install_requires,
      test_suite='nose2.collector.collector',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/KrishnaswamyLab/MAGIC',
      download_url="https://github.com/KrishnaswamyLab/scgraph/archive/v{}.tar.gz".format(
          version),
      keywords=['big-data',
                'manifold-learning',
                'computational-biology'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Framework :: Jupyter',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ]
      )
