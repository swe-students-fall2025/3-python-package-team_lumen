import random
import sys
from pathlib import Path

# Add parent directory to path if running as script
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from morseify.core import encode, decode, is_valid
except ModuleNotFoundError:
    from .core import encode, decode, is_valid

# List of sentences for the quiz
QUIZ_SENTENCES = [
    "HELLO WORLD",
    "LET US TRY",
    "MORSE CODE IS FUN",
    "PYTHON ROCKS",
    "LEARNING TAKES TIME",
    "FORZA ROMA",
    "SWE IS USEFUL",
    "RUNNING OUT OF IDEAS",
    "THIS SHOULD BE ENOUGH",
    "I AM NOT VERY CREATIVE"
]


def quiz(sentence=None, mode=None):
    """
    Interactive morse code quiz.
    
    Args:
        sentence: Optional - specific sentence to use, or None for random
        mode: Optional - 'reading' or 'writing', or None to ask
    """
    if sentence is None:
        selected_sentence = random.choice(QUIZ_SENTENCES)
    else:
        selected_sentence = sentence.upper().strip()
    

    # Ask for mode if not provided
    if mode is None:
        print("\n" + "=" * 60)
        print("MORSE CODE QUIZ")
        print("=" * 60)
        print("Choose your mode:")
        print("'reading'  - Decode morse code → text")
        print("'writing'  - Encode text → morse code")
        print()
        mode = input("Enter the mode ('reading' or 'writing'): ").strip().lower()
        
        while mode not in ['reading', 'writing']:
            print("\nInvalid mode!")
            print("Please enter 'reading' or 'writing'")
            mode = input("\nEnter the mode: ").strip().lower()
    
    print("\n" + "=" * 60)
    if mode == 'reading':
        print("READING MODE: Decode morse code → text")
        print("=" * 60)
        morse_to_decode = encode(selected_sentence)
        print(f"\nMorse code: {morse_to_decode}")
        print()
        answer = input("Your answer: ").upper().strip()
        
        if answer == selected_sentence:
            print("\nCorrect! Well done!")
        else:
            print("\nIncorrect!")
    
    else:  # writing mode
        print("WRITING MODE: Encode text → morse code")
        print("=" * 60)
        print(f"\nText to encode: {selected_sentence}")
        print()
        
        answer = input("Your answer: ").strip()
        while not is_valid(answer):
            print("\nInvalid morse code format!")
            print("Please use only dots (.), dashes (-), spaces, and slashes (/)")
            print("Example: ... --- ... (for SOS)")
            answer = input("\nYour answer: ").strip()
        
        # Now check if the valid morse code is correct
        if answer == encode(selected_sentence):
            print("\nCorrect! Well done!")
        else:
            print("\nIncorrect!")
    
    print("=" * 60)


if __name__ == "__main__":
    quiz()