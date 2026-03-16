# Lambda e basicamente criar uma funcao anonima
# Usar lambda para verificar se o len da string e maior que o N(sys.argv[2])
# Usar list compreenhension para fazer a lista que vai ser retornada
import sys


def main():
    argc = len(sys.argv)
    assert argc == 3, "the arguments are bad"

    try:
        size = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad") from None

    splitString = sys.argv[1].split()
    res = [s for s in splitString if (lambda x: len(x) > size)(s)]
    print(res)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
