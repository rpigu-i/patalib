from setuptools import setup, find_packages


setup(
    name='patalib',
    version='2.0.0',
    description='Pataphysics library',
    maintainer='patamechanix',
    license='MIT',
    url='https://github.com/patamechanix/patalib',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
        'nltk>=3.4.5',
        'hypothesis>=5.16.0'

    ]
)

