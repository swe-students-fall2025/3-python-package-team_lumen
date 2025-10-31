from .core import encode, decode, is_valid, explain


def main():
    print("Morse Code Demo")
    text = "HELLO WORLD"
    encoded = encode(text)
    decoded = decode(encoded)
    print(f"Original: {text}")
    print(f"Encoded : {encoded}")
    print(f"Decoded : {decoded}")
    # print(f"Valid?   {is_valid(encoded)}")
    # print(f"Explain : {explain(encoded)}")

if __name__ == "__main__":
    main()