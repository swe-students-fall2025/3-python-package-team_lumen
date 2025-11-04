from .core import encode, decode, is_valid
from .explain import explain
from .quiz import quiz


def main():
    print("MORSE CODE PACKAGE - DEMO")
    
    # Encode/Decode Test Section

    print("ENCODE/DECODE TEST")
    test_cases = [
        "HELLO",
        "HELLO WORLD",
        "SOS",
        "PYTHON",
        "123",
        "A1B2C3"
    ]
    
    for text in test_cases:
        encoded = encode(text)
        decoded = decode(encoded)
        
        print(f"\nOriginal: '{text}'")
        print(f"Encoded : '{encoded}'")
        print(f"Decoded : '{decoded}'")
        
        # Check if round-trip works
        if decoded == text:
            print("✓ Round-trip successful!")
        else:
            print(f"✗ Round-trip failed! Expected: '{text}'")

    print("\n" + "=" * 60)
    print("EXPLAIN FEATURE DEMO")
    
    explain_examples = [
        ".... . .-.. .-.. ---",
        ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
        "... --- ...",
        ".--. -.-- - .... --- -."
    ]
    
    for i, morse_code in enumerate(explain_examples, 1):
        print(f"\nExample {i}:")
        explanation = explain(morse_code)
        print(explanation)
    
    

    print("\n" + "=" * 60)
    print("QUIZ FEATURE DEMO")
    print("\nThe quiz feature is interactive and allows you to practice:")
    print("  - Reading mode: Decode morse code → text")
    print("  - Writing mode: Encode text → morse code")
    print("\nStarting interactive quiz...")
    
    # Start the quiz (it will handle all user interaction)
    quiz()


if __name__ == "__main__":
    main()