from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='iqbio.xdvtheme',
      version=version,
      description="A theme for IQBIO",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme xdv',
      author='Kurt Bendl',
      author_email='kurt@tool.net',
      url='http://github.com/itd/iqbio.xdvtheme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iqbio'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
