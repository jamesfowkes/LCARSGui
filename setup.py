#!/usr/bin/env python

from distutils.core import setup

setup(name='LCARSGui',
      version='1.0',
      description='LCARS style GUI for Python. Requires pygame',
      author='James Fowkes',
      author_email='jamesfowkes@gmail.com',
      url='http://www.github.com/jamesfowkes/lcarsgui/',
	  packages=['LCARSGui'],
      package_dir={'LCARSGui':'.'},
	  package_data={'LCARSGui':['data/*']}
	  )