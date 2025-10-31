"""
Morse Code Package
A Python package for encoding and decoding Morse code with additional utilities.
"""

from morse_code.core import (
    encode,
    decode,
    is_valid,
    normalize_text,
    normalize_code,
    explain,
    quiz
)

__all__ = [
    'encode',
    'decode',
    'is_valid',
    'normalize_text',
    'normalize_code',
    'explain',
    'quiz'
]

