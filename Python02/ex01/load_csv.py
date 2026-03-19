import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Function to load a csv

    Args:
        path (str): Path to the file to load

    Returns:
        None: If the file in itself has any errors or cant be openned
        data (pd.DataFrame): DataFrame from the file provided

    Raises:
        Exceptions: If any problem happens it will be risen
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
