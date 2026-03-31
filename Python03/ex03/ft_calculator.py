class calculator:
    def __init__(self, values):
        """
        Initialize the calculator with a list of values.

        Args:
            values (list[float]): List of numerical values.

        Returns:
            None
        """
        self.values = values

    def __add__(self, object) -> None:
        """
        Add a scalar value to each element of the list.

        Args:
            object (float): Value to add to each element.

        Returns:
            None
        """
        self.values = [v + object for v in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """
        Multiply each element of the list by a scalar value.

        Args:
            object (float): Value to multiply each element by.

        Returns:
            None
        """
        self.values = [v * object for v in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """
        Subtract a scalar value from each element of the list.

        Args:
            object (float): Value to subtract from each element.

        Returns:
            None
        """
        self.values = [v - object for v in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """
        Divide each element of the list by a scalar value.

        Args:
            object (float): Value to divide each element by.

        Returns:
            None

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        if object == 0:
            raise ZeroDivisionError("Division by 0 detected")
        self.values = [v / object for v in self.values]
        print(self.values)


def main():
    print()


if __name__ == "__main__":
    main()
