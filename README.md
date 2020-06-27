# Hello World

This is an example project demonstrating how to publish a python module to PyPI

## Installation

```python
pip3 install helloworld
```

## Usage

```python
from helloworld import say_hello

# Generate "hello, foo!"
say_hello("foo")
```

# Developing Hello World

To install helloworld, along with the tools you need to dev and test, run the following in your virtualenv:

```bash
$ pip3 install -e .[dev]
```
