from setuptools import setup, find_packages


setup(
    name='patalib',
    version='2.1.0',
    description='Pataphysics library',
    maintainer='rpigu-i',
    license='MIT',
    url='https://github.com/rpigu-i/patalib',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
        'nltk>=3.9.1',
        'hypothesis>=5.16.0'

    ]
)

