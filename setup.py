# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'mock',
    'pyyaml',
]
dependency_links = [

]

if __name__ == '__main__':
    setup(name='Toster',
          description='unittest wrapper with ready to configure command line',
          version='0.1.2',
          packages=find_packages('src'),
          package_dir={'': 'src'},
          install_requires=install_requires,
          dependency_links=dependency_links,
          include_package_data=True,
          entry_points="""\

          """,
          )
