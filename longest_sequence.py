"""Problem 3: Find a longest alternating increasing sequence."""

import sys
from pathlib import Path


def longest_sequence(a, b):
    # Each length describes the best sequence ending at that array index.
    length_a = [1] * len(a)
    length_b = [1] * len(b)
    previous_a = [-1] * len(a)
    previous_b = [-1] * len(b)

    best_length = 0
    best_index = -1
    ends_in_a = True

    for i in range(max(len(a), len(b))):
        if i < len(a):
            for j in range(min(i, len(b))):
                if b[j] < a[i] and length_b[j] + 1 > length_a[i]:
                    length_a[i] = length_b[j] + 1
                    previous_a[i] = j
            if length_a[i] > best_length:
                best_length = length_a[i]
                best_index = i
                ends_in_a = True

        if i < len(b):
            for j in range(min(i, len(a))):
                if a[j] < b[i] and length_a[j] + 1 > length_b[i]:
                    length_b[i] = length_a[j] + 1
                    previous_b[i] = j
            if length_b[i] > best_length:
                best_length = length_b[i]
                best_index = i
                ends_in_a = False

    # Follow the saved indices backwards, switching arrays at each step.
    sequence = []
    while best_index != -1:
        if ends_in_a:
            sequence.append(a[best_index])
            best_index = previous_a[best_index]
        else:
            sequence.append(b[best_index])
            best_index = previous_b[best_index]
        ends_in_a = not ends_in_a
    sequence.reverse()
    return sequence


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python longest_sequence.py INPUT_FILE [INPUT_FILE ...]")

    for index, filename in enumerate(sys.argv[1:]):
        path = Path(filename)
        with path.open(encoding="utf-8") as input_file:
            size_a = int(input_file.readline())
            size_b = int(input_file.readline())
            a = list(map(int, input_file.readline().split()))
            b = list(map(int, input_file.readline().split()))
        if len(a) != size_a or len(b) != size_b:
            sys.exit(f"Array sizes do not match the header in {path.name}")

        if index > 0:
            print()
        print(f"File Input: {path.name}")
        print(f"Longest Sequence: {len(longest_sequence(a, b))}")


if __name__ == "__main__":
    main()
