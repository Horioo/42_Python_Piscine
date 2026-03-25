# nonlocal - variavel da funcao exterior, só existe dentro
# da cadeia das funcoes

# ** - Operador Exponencia


def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    return inner
