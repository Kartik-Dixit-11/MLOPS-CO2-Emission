import setuptools

__version__='1.0.0'

SRC='Regression'

setuptools.setup(
    name=SRC,
    version=__version__,
    author='Kartik',
    author_email='kartik.dixit410@gmail.com',
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)
