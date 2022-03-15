'''
setup.py: cif-data-concentration module repository
'''
from distutils.core import setup

setup(
      name='cif-data-concentration',
      version='1.0',
      description='A useful package to extract data from .cif file and compile the data to dataframe.
      Different machine learning methods to predict bandgap when crystal lattice constant known',
      author='Yifei He, Ruofan Liu, Yanyao Han, Jiayi Li',
      url='',
      packages=['distutils', 'distutils.command'],
      license='',
      keywords=[
            'cif',
            'dataframe',
            'bandgap',
            'crystal lattice constant',
            'machine_learning',
      ],
      python_requires='>=3.7',
     )
