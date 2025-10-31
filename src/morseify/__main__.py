from .core import encode, decode, is_valid
from .explain import explain


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

    # text = input("Enter text to encode: ")
    # encoded = encode(text)
    # print("Encoded:", encoded)
    # print("Decoded back:", decode(encoded))

if __name__ == "__main__":
    main()