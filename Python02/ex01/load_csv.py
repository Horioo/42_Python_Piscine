import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame | None: The loaded dataset as a DataFrame.
        Returns None if the file cannot be opened or read.

    Notes:
        Prints the shape of the dataset in the format (rows, columns).
    """
    try:
        data = pd.read_csv(path)
    except Exception:
        return None

    print(f"Loading dataset of dimensions {data.shape}")
    return data


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
