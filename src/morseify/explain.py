from morseify.mapping import MORSE_TO_LETTER, LETTER_TO_MORSE
from morseify.core import is_valid
from morseify.normalize import normalize_code

def explain(morse_message):
    # TODO: Implement explanation logic
    """
    WantToDo in explain.py
    Provide a step-by-step breakdown of a morse code input.

    Args:
        morse_message: Morse code string need to be explained
        
    Returns:
        String containing the step-by-step breakdown
    """
    #Step 1: input validation
    if not is_valid(morse_message):
        return "Error: Invalid Morse code message. Please check the format."
    
    #Step 2: Normalize the morse code
    normalized = normalize_code(morse_message)
    
    pass