# Slicing envolves using the [:::]
# where the first will be the start of the slice
# the second the end of the slice
# the third the steps, basically if we put 2 it wll do the elements 0 2 4...
# If the value is negative it starts from the end and ignores thoses values
# for example the -2 will ignore the last 2 results

import numpy as np
import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a List

    Args:
        family: The list to be sliced
        start: Index to start the slice
        end: Index to end the slice

    Returns:
        Sliced List
    """
    try:
        if not isinstance(family, list):
            raise TypeError("The Object is not a list")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All elements of the list must also be lists")
        if not all(len(row) == len(family[0]) for row in family):
            raise ValueError("Not all elements are the same size")
    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(0)
    except TypeError as e:
        print(f"TypeError: {e}")
        sys.exit(0)

    f_arr = np.array(family, dtype=float)
    print(f"My shape is : {f_arr.shape}")
    f_arr = f_arr[start:end]
    print(f"My new shape is : {f_arr.shape}")
    return f_arr.tolist()


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7, 100],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
