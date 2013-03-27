#!/usr/bin/env python

from distutils.core import setup

setup(name='MiniGraph',
      version='.1',
      description='Graph class with SSSP',
      author='Erik Gafni',
      author_email='egafni@gmail.com',
      url='http://github.com/egafni/MiniGraph/',
      packages=['minigraph'],
      )

from networkx.algorithms import sho