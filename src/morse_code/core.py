def encode(text):
    """
    Convert English text to morse code.
    
    Args:
        text: English text string to encode
        
    Returns:
        Morse code string
    """
    from morse_code.mapping import LETTER_TO_MORSE
    
    # Normalize the text first(delete after normalize function is implemented)
    if text is None:
        return None
    normalized = text.upper().strip() 

    # change to this:
    # normalized = normalize_text(text)
    
    # Convert each character to morse code
    result = []
    for char in normalized:
        if char == ' ':
            # Space between words becomes ' / '
            result.append('/')
        else:
            # Get morse code for character
            morse_char = LETTER_TO_MORSE.get(char, '')
            if morse_char:
                result.append(morse_char)
    
    # Join with spaces between letters
    return ' '.join(result)


def decode(morse_code):
    # TODO: Implement decoding logic: convert morse code to English
    pass


def is_valid(morse_code):
    # TODO: Implement validation logic
    pass





