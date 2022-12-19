NUMBER = {"1", "2", "3"}
ALPHABET = {"A", "B", "C"}

def main() -> None:
    words = "A 1 B".split()

    alphabet_counter = len(ALPHABET.intersection(words))
    number_counter = len(NUMBER.intersection(words))

    print(f'Alphabet counter : {alphabet_counter}')
    print(f'Number counter : {number_counter}')


if __name__ == "__main__":
    main()