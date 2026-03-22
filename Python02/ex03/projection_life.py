from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def strtoint(string: str):
    """
    Convert a formatted numeric string into an integer.

    This function handles population values that may include suffixes
    such as 'M' (millions) and converts them into their integer
    representation. It also safely handles missing or invalid values.

    Args:
        string (str): The input string representing a numeric value.
                      Examples: "6.98M", "1000000", "NaN", "".

    Returns:
        int: The numeric value converted to an integer.
             - "6.98M" -> 6980000
             - "1000000" -> 1000000
             - "NaN" or empty string -> 0

    Raises:
        ValueError: If the string cannot be converted into a valid number.

    Notes:
        - Currently supports values in millions ('M').
        - Missing or invalid values such as "" or "NaN" are converted to 0.
    """
    if not string or string == "NaN":
        return 0
    if string.endswith('M'):
        return int(float(string[:-1]) * 1_000_000)
    if string.endswith('K'):
        return int(float(string[:-1]) * 1_000)
    if string.endswith('B'):
        return int(float(string[:-1]) * 1_000_000_000)
    return int(string)


def project_life_graph():
    data_income: pd.DataFrame \
        = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data_life: pd.DataFrame = load("life_expectancy_years.csv")

    if "1900" not in data_income.columns or "1900" not in data_life.columns:
        raise ValueError("Year 1900 not found in dataset")

    data_income["country"] = data_income["country"].str.strip()
    data_life["country"] = data_life["country"].str.strip()

    data_income = data_income[["country", "1900"]].rename(
        columns={"1900": "x"}
    )
    data_life = data_life[["country", "1900"]].rename(
        columns={"1900": "y"}
    )

    merged: pd.DataFrame = pd.merge(data_income, data_life,
                                    on="country").dropna()

    merged.plot.scatter(x="x", y="y")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1K", "10K"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("GDP and Life Expectancy on the year 1900")
    plt.show()


def main():
    project_life_graph()


if __name__ == "__main__":
    main()
