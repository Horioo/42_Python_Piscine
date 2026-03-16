# List compreehension usado para criar uma lista que itera
# por cada elemento e depois faz a verificacao com a funcao passada
# yield from, usado para returnar um iterador porque e assim que o
# filter() faz, tive de usar from para retornar cada item indivualmente porque
# sem o from iria retornar a lista completa mas dentro de outra lista

def ft_filter(function, iterable) -> filter:
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function is not None and not callable(function):
        raise TypeError("function must be callable")

    try:
        iter(iterable)
    except TypeError:
        raise TypeError("iterable must be iterable")

    if function is None:
        result = [x for x in iterable if x]
    else:
        result = [x for x in iterable if function(x)]
    yield from result


def is_even(number):
    return number % 2 == 0


def main():
    print(ft_filter.__doc__)
    test = [42, 35, 21, 8]
    final = ft_filter(is_even, test)
    print(list(final))


if __name__ == "__main__":
    main()
