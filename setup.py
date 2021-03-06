from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='helloworld_jw',
    version='0.0.1',
    description='say hello!',
    py_modules=['helloworld', 'f2'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires = [
        "pandas"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
