from typing import Any

# mean = Media
# median = Mediano
# quartile = Quartis
# var = Variance = Quao longe os valores estao da media (Mas ao Quadrado)
# std = Standard Deviation = Quao longe os valores estao da media
# (Valores Originais)

# *  e **, não sao pointers, significam que podemos receber
# um numero arbitrário de argumentos


def mean(args) -> int | float:
    """
    Compute the mean (average) of a list of numbers.

    Args:
        args (list[int | float]): List of numerical values.

    Returns:
        int | float: The mean of the values.
    """
    res = 0
    for v in args:
        res += v
    res /= len(args)
    return res


def median(args) -> int | float:
    """
    Compute the median value of a list of numbers.

    Args:
        args (list[int | float]): List of numerical values.

    Returns:
        int | float: The median value.
    """
    args.sort()
    if len(args) % 2 == 0:
        i = int(len(args) / 2) - 1
        avg = (args[i] + args[i + 1]) / 2
        return avg
    else:
        return args[int((len(args)) / 2)]


def quartile(args) -> list[int | float]:
    """
    Compute the first and third quartiles of a list of numbers.

    Args:
        args (list[int | float]): List of numerical values.

    Returns:
        list[float]: A list containing the first and third quartiles.
    """
    args.sort()
    quartile = []
    quartile.append(float(args[int(len(args) / 4)]))
    quartile.append(float(args[int((3 * len(args)) / 4)]))
    return quartile


def variance(args) -> int | float:
    """
    Compute the variance of a list of numbers.

    Args:
        args (list[int | float]): List of numerical values.

    Returns:
        float: The variance of the values.
    """
    m = mean(args)
    dif = []
    for v in args:
        dif.append((v - m) * (v - m))
    sum_squares = sum(dif)
    var = sum_squares / len(args)
    return var


def std(args) -> int | float:
    """
    Compute the standard deviation of a list of numbers.

    Args:
        args (list[int | float]): List of numerical values.

    Returns:
        float: The standard deviation of the values.
    """
    var = variance(args)
    standard_deviation = var ** 0.5
    return standard_deviation


def protections(args) -> bool:
    """
    Check if all elements in the list are numeric.

    Args:
        args (list[Any]): List of values to validate.

    Returns:
        bool: True if any value is not int or float, False otherwise.
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            return True
    return False


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Compute and print statistical operations based on provided arguments.

    Args:
        *args (Any): Numerical values for calculations.
        **kwargs (Any): Named operations to perform. Supported values are:
            "mean", "median", "quartile", "std", "var".

    Returns:
        None
    """
    for key, value in kwargs.items():
        if len(args) == 0 or len(kwargs) == 0 or protections(args):
            print("ERROR")
        else:
            match(value):
                case "mean":
                    print(f"mean : {mean(list(args))}")
                case "median":
                    print(f"median : {median(list(args))}")
                case "quartile":
                    print(f"quartile : {quartile(list(args))}")
                case "std":
                    print(f"std : {std(list(args))}")
                case "var":
                    print(f"var : {variance(list(args))}")
                case _:
                    return None
