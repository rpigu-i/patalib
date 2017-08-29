from setuptools import setup, find_packages


setup(
    name='patalib',
    version='1.0.1',
    description='Pataphysics library',
    maintainer='patamechanix',
    license='MIT',
    url='https://github.com/patamechanix/patalib',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
        'nltk==2.0.5',
        'hypothesis==3.4.2'

    ]
)

