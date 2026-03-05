import sys


def countStuff(string: str):
    """
    Function to count how many Upper Letters, lower Letters,
    punctuation, spaces and digits a string has
    """

    upperLetters = sum(1 for c in string if c.isupper())
    lowerLetters = sum(1 for c in string if c.islower())
    punctuation = sum(1 for c in string if c in "'.,;:?!")
    spaces = sum(1 for c in string if c.isspace())
    digits = sum(1 for c in string if c .isdigit())
    all = upperLetters + lowerLetters + punctuation + spaces + digits

    print(f"The text contains {all} characters:\n \
        {upperLetters} upper letters\n \
        {lowerLetters} lower letters\n \
        {punctuation} punctuation marks\n \
        {spaces} spaces\n \
        {digits} digits"
        )

# ToDo Try and Except on this main()
def main():
    argc = len(sys.argv)
    assert argc == 2 or argc == 1, "more than one argument is provided"
    if argc == 1 or sys.argv[1] == "":
        testString = input("What is the text to count?\n")
    else:
        testString = sys.argv[1]
    countStuff(testString)


if __name__ == "__main__":
    main()
