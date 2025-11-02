import pytest
from morseify.core import is_valid

def test_valid_single():
    assert is_valid("....") is True  
    assert is_valid(".") is True
    assert is_valid("-.--") is True
    
    assert is_valid("-...") is True
    assert is_valid(".-.") is True
    assert is_valid("---") is True

def test_valid_multiple():
    morse1 = ".... . -.-- / -... .-. ---"           
    morse2 = ".. / .-- .- -. - / .- / -.-. .- -"   
    assert is_valid(morse1) is True
    assert is_valid(morse2) is True
