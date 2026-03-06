import sys


def to_morse_code(s):
    """
Transform the string s into Morse Code via the use of a dictionary
    """

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ",
        "D": "-.. ", "E": ". ", "F": "..-. ",
        "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ",
        "S": "... ", "T": "- ", "U": "..- ",
        "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "Ç": "-.-.. ",
        "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ", "8": "---.. ", "9": "----. ",
        "0": "----- ",
    }
    result = ""
    for c in s:
        result += NESTED_MORSE[c.upper()]
    print(result)


def is_valid(s):
    """
Check if the string is only composed of alphanumerics or spaces
    """
    return all(c.isalnum() or c.isspace() for c in s)


def main():
    try:
        argc = len(sys.argv)
        assert argc == 2, "the arguments are bad"
        if not is_valid(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        to_morse_code(sys.argv[1])

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
