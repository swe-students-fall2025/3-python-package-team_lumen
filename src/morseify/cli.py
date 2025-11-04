"""
Command-line interface for morseify.
"""

import sys
from morseify.core import encode, decode, is_valid
from morseify.explain import explain
from morseify.quiz import quiz


def cli():
    """
    Command-line interface for morseify.
    Auto-detects whether input is text (encode) or morse code (decode).
    Supports --explain flag for step-by-step breakdown.
    
    Usage:
        morseify "HELLO"           # Encodes text to morse code
        morseify ".... . .-.. .-.. ---"  # Decodes morse code to text
        morseify --explain ".... . .-.. .-.. ---"  # Explains morse code
        morseify -e ".... . .-.. .-.. ---"  # Short form for explain
    """
    if len(sys.argv) < 2:
        print("Usage: morseify [--explain|-e] <text or morse code>")
        print("Examples:")
        print('  morseify "HELLO"')
        print('  morseify ".... . .-.. .-.. ---"')
        print('  morseify --explain ".... . .-.. .-.. ---"')
        print('  morseify -e ".... . .-.. .-.. ---"')
        sys.exit(1)
    
    # Check for explain flag
    explain_mode = False
    args = sys.argv[1:]
    
    if args[0] in ['--explain', '-e']:
        explain_mode = True
        args = args[1:]  # Remove the flag
    
    if not args:
        print("Error: No input provided after flag.")
        print("Usage: morseify --explain <morse code>")
        sys.exit(1)
    
    # Join all arguments in case user passes multiple words
    input_text = ' '.join(args)
    
    # If explain mode is requested
    if explain_mode:
        result = explain(input_text)
        print(result)
        return
    
    # Auto-detect: if input contains only morse characters (., -, /, space), decode it
    # Otherwise, encode it
    valid_morse_chars = {'.', '-', '/', ' '}
    is_morse = all(char in valid_morse_chars for char in input_text) and input_text.strip()
    
    if is_morse and is_valid(input_text):
        # It's valid morse code, decode it
        result = decode(input_text)
        print(result)
    else:
        # It's text, encode it
        result = encode(input_text)
        print(result)

