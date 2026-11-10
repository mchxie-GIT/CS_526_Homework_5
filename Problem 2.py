import sys
from pathlib import Path


VOWEL_CODES = (".-", ".", "..", "---", "..-")


def count_vowel_combinations(symbols):
    # ways[i] counts decodings of the first i symbols.
    ways = [0] * (len(symbols) + 1)
    ways[0] = 1

    for end in range(1, len(symbols) + 1):
        for code in VOWEL_CODES:
            start = end - len(code)
            if start >= 0 and symbols[start:end] == code:
                ways[end] += ways[start]

    return ways[-1]


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python vowel_combinations.py INPUT_FILE [INPUT_FILE ...]")

    for index, filename in enumerate(sys.argv[1:]):
        path = Path(filename)
        size, *pieces = path.read_text(encoding="utf-8").split()
        symbols = "".join(pieces)
        if len(symbols) != int(size) or set(symbols) - {".", "-"}:
            sys.exit(f"Invalid Morse input in {path.name}")

        if index > 0:
            print()
        print(f"File Input: {path.name}")
        print("The Number of Vowel combinations is:")
        print(f"    {count_vowel_combinations(symbols)}")


if __name__ == "__main__":
    main()
