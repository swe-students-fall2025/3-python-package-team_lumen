from .core import encode, decode, is_valid
from .explain import explain


def main():
    print("Morse Code Encode/Decode Test")
    # Test cases
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
    
    # Uncomment for interactive mode
    # print("\nInteractive mode:")
    # text = input("Enter text to encode: ")
    # encoded = encode(text)
    # print(f"Encoded: {encoded}")
    # decoded = decode(encoded)
    # print(f"Decoded: {decoded}")

if __name__ == "__main__":
    main()