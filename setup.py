from setuptools import setup, find_packages


setup(
    name='patalib',
    version='1.0.0',
    description='Pataphysics library',
    maintainer='Andy Dennis',
    license='MIT',
    url='https://github.com/andydennis/patalib',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
        'nltk==2.0.5',
        'hypothesis==3.4.2'

    ]
)

