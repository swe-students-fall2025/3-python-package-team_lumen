import pytest
from morseify.core import is_valid

def test_valid_single():
    assert is_valid("....") is True  
    assert is_valid(".") is True
    assert is_valid("-.--") is True
    
    assert is_valid("-...") is True
    assert is_valid(".-.") is True
    assert is_valid("---") is True


