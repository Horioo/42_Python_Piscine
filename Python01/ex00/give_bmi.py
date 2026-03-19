# Erros:
# Lists not the same size
# Lists not int or float
# Not Lists?

# numpy - Library used to work with arrays and advanced Math
# that is way faster than normal python since it uses
# C as its base

def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate BMI for each pair of height and weight.

    Args:
        height: Heights in meters.
        weight: Weights in kilograms.

    Returns:
        List of BMI values.
    """
    try:
        assert len(height) == len(weight), "Both Lists have to be equal \
in Size"

        for h, w in zip(height, weight):
            assert isinstance(h, (int, float)), \
                f"Height Value is not Float or Int({h})"
            assert isinstance(w, (int, float)), \
                f"Weight Value is not Float or Int({w})"
            assert w > 0 and h > 0, "Negative or Zero Values"
            assert 0.55 < h < 2.73, f"Height Value is to low or to High({h})"

        return [w / (h * h) for h, w in zip(height, weight)]
    except AssertionError as e:
        raise Exception(f"AssertionError: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply limit to each value of BMI.

    Args:
        bmi: BMI values
        limit: Limit to impose

    Returns:
        List of Boolean
    """
    return [value > limit for value in bmi]


def main():
    height = [1.75, 1.34, 3.54, 2.10, 1.50, 2.00, 1.80, 1.65, 2.50]
    weight = [71.0, 65.0, 1.0, 201.0, 11.0, 151.0, 301.0, 55.0, 121.0]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
