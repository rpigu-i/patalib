from setuptools import setup, find_packages


setup(
    name='patalib',
    version='0.0.1',
    description='Pataphysics library',
    long_description=open('README.md', 'r').read(),
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

