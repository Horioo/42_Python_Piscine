from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


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
    string = string.strip()
    if not string or string == "NaN":
        return 0
    if string.endswith('K'):
        return int(float(string[:-1]) * 1_000)
    if string.endswith('M'):
        return int(float(string[:-1]) * 1_000_000)
    if string.endswith('B'):
        return int(float(string[:-1]) * 1_000_000_000)
    return int(string)


def compare_campus_graph(campus1: str, campus2: str):
    """
    Load population data and display a comparative graph between two countries.

    This function reads a CSV dataset containing population values per country
    across multiple years, filters the data for the two specified countries,
    and plots their population evolution over time.

    The dataset is truncated to the year 2050 if available, and values are
    converted from formatted strings (e.g., "6.9M") into integers
    before plotting.

    Args:
        campus1 (str): Name of the first country to compare.
        campus2 (str): Name of the second country to compare.

    Raises:
        FileNotFoundError: If the dataset file cannot be found.
        ValueError:
            - If one or both countries are not present in the dataset.
            - If there is a mismatch between years and population data.
        RuntimeError: If the dataset cannot be parsed correctly.
        Exception: For any unexpected errors during execution.

    Notes:
        - The CSV file must have the following structure:
            - First column: country names
            - Remaining columns: years (e.g., 1800, 1801, ..., 2100)
        - Population values may include suffixes 'M' and
          are converted to integers using the `strtoint` helper function.
        - The x-axis displays years at regular intervals
        (default: every 40 years).
        - The y-axis is dynamically scaled based on the
        maximum population value.
    """
    data: pd.DataFrame = load("population_total.csv")

    if "2050" in data.columns:
        data = data.loc[:, data.columns[:data.columns.get_loc("2050") + 1]]

    data["country"] = data["country"].str.strip()

    country1_data = data[data["country"] == campus1]
    country2_data = data[data["country"] == campus2]

    if country1_data.empty or country2_data.empty:
        raise ValueError("One of the countries was not found")

    country1_population = [strtoint(c) for c in country1_data.iloc[0, 1:]]
    country2_population = [strtoint(c) for c in country2_data.iloc[0, 1:]]

    years = [int(y) for y in data.columns[1:]]

    if len(years) != len(country1_population) or \
            len(years) != len(country2_population):
        raise ValueError("Mismatch between years and population data")

    min_year = min(years)
    max_year = max(years)
    step = 40

    years_ticks = list(range(min_year, max_year + 1, step))

    max_population = max(max(country1_population), max(country2_population))

    step = max(1, max_population // 3)

    population_numbers = [step, step * 2, step * 3]
    population_ticks = [f"{int(p / 1_000_000)}M" for p in population_numbers]

    plt.plot(years, country1_population, label=f'{campus1}')
    plt.plot(years, country2_population, label=f'{campus2}')
    plt.xticks(years_ticks, labels=[str(t) for t in years_ticks])
    plt.yticks(population_numbers, population_ticks)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"Population Projections {campus1} vs {campus2}")
    plt.legend(loc='lower right')
    plt.show()


def main():
    try:
        compare_campus_graph("Portugal", "China")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
