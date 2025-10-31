"""
Morse Code Package
A Python package for encoding and decoding Morse code with additional utilities.
"""

from morse_code.core import (
    encode,
    decode,
    is_valid
)
from morse_code.normalize import (
    normalize_text,
    normalize_code
)
from morse_code.explain import explain
from morse_code.quiz import quiz

__all__ = [
    'encode',
    'decode',
    'is_valid',
    'normalize_text',
    'normalize_code',
    'explain',
    'quiz'
]

