import random
import sys
from pathlib import Path

# Add parent directory to path if running as script
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from morseify.core import encode, decode
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
    

    if mode is None:
        mode = input("Enter the mode: 'reading' or 'writing': ")
        while mode not in ['reading', 'writing']:
            print()
            print("Invalid mode. Please enter 'reading' or 'writing'")
            print("Please try again.")
            print()
            mode = input("Enter the mode: 'reading' or 'writing': ")
    
    if mode == 'reading':
        print(f"Your sentence in morse code is: {encode(selected_sentence)}")
        answer = input("Enter the answer: ").upper().strip()
        if answer == (selected_sentence):
            print("Correct!")
        else:
            print("Incorrect!")
    else:
        print(f"Writing mode: {selected_sentence}")
    
    # TODO: Rest of quiz logic
    pass


if __name__ == "__main__":
    quiz()