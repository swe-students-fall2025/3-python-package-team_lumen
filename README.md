[![CI / CD](https://github.com/swe-students-fall2025/3-python-package-team_lumen/actions/workflows/build.yml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_lumen/actions/workflows/build.yml)

## morseify - Overview
morseify is a lightweight Python package that brings the world of Morse code to anyone curious about how digital communication began. It offers intuitive encode and decode functionality to translate between English text and Morse code, along with built-in tools for text normalization and message validation.

For a more interactive experience, morseify also includes a quiz mode that generates random Morse code challenges for users to decode, making it both an educational and entertaining way to explore the fundamentals of encoded communication.

## Features
- Encode English text to Morse code  
- Decode Morse code to English text  
- Normalize text and Morse sequences  
- Validate Morse message formats  
- Explain message steps
- Quiz mode to test Morse knowledge 

## Team Members
- [Coco Liu](https://github.com/yiminliu2004)  
- [Angela Gao](https://github.com/Xuan4781)  
- [Phoebe Huang](https://github.com/phoebelh)  
- [Galal Bichara](https://github.com/gkbichara)
- [Leo Qian](https://github.com/Leo-codingMaster)  

## Installation / Setup

<!-- TODO: Update once package is published to PyPI or ready for local install.
Include both PyPI and local development setup -->

## Using morseify in Your Code
You can import and use Morseify. Here's documentation for all available functions:

### Core Functions

```python
from morseify import encode, decode, is_valid

text = "HELLO WORLD"
morse = encode(text)
print(morse)

decoded = decode(morse)
print(decoded)

print(is_valid(morse))
```

## Example Program

See our complete example program that demonstrates all functions: 

```python

```

## Contributing to Morseify
### Development Workflow
### Project Structure
### Running Tests

## PyPI Package

This package is available on PyPI: [morseify-lumen](https://pypi.org/project/morseify-lumen/).
