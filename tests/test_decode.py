from morseify.core import decode


def test_decode_single_letter():
    """Test decoding a single letter."""
    assert decode(".-") == "A"
    assert decode("-") == "T"
    assert decode("...") == "S"


def test_decode_word():
    """Test decoding a word."""
    assert decode(".... . .-.. .-.. ---") == "HELLO"
    assert decode("... --- ...") == "SOS"


def test_decode_multiple_words():
    """Test decoding multiple words with separator."""
    assert decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..") == "HELLO WORLD"
    assert decode("... --- ... / .... . .-.. .--.") == "SOS HELP"


def test_decode_numbers():
    """Test decoding numbers."""
    assert decode(".---- ..--- ...--") == "123"
    assert decode("-----") == "0"


def test_decode_invalid_morse_code():
    """Test decoding invalid morse code returns error message."""
    assert decode("---.") == "Morse code is not valid"  # Invalid sequence not in mapping
    assert decode("ABC") == "Morse code is not valid"  # Contains invalid characters
    assert decode("....X") == "Morse code is not valid"  # Contains invalid character
    assert decode("") == "Morse code is not valid"  # Empty string
    assert decode("   ") == "Morse code is not valid"  # Only spaces


def test_decode_mixed_valid_invalid():
    """Test decoding morse code with invalid sequences."""
    assert decode(".... . .-.. .-.. --- ---.") == "Morse code is not valid"  # Has invalid sequence


def test_decode_with_punctuation():
    """Test decoding morse code with punctuation."""
    assert decode(".... . .-.. .-.. --- .-.-.-") == "HELLO."
    assert decode("-- ..- .-.. - .. .--. .-.. .") == "MULTIPLE"


def test_decode_normalized_input():
    """Test decoding already normalized morse code."""
    # decode should handle normalization internally
    assert decode("  .... . .-.. .-.. ---  ") == "HELLO"  # Extra spaces