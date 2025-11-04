'''
This demo will showcase the core functionalities:
- Encoding
- Decoding
- Normalization
- Validate
- Explaining
- Quiz
'''

from morseify import encode, decode, normalize_text, normalize_code, is_valid, explain, quiz

def main():
    print("Demo")

    # encode & decode
    text = "HELLO WORLD"
    encoded = encode(text)
    decoded = decode(encoded)
    print(f"Original: {text}")
    print(f"Encoded : {encoded}")
    print(f"Decoded : {decoded}\n")

    # normalization
    messy_text = "HeLLo   WoRLd!!!"
    print("Normalized text:", normalize_text(messy_text))
    print("Normalized code:", normalize_code(".... . .-.. .-.. --- / .-- --- .-. .-.. -..  "))

    # validating
    print("\nValid Morse?", is_valid(encoded))

    # explain
    print("\nExplain:")
    print(explain(encoded))

    # quiz
    print("\nQuiz (read & write):")
    quiz()

if __name__ == "__main__":
    main()
