from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def load_graph(country: str):
    """
    Load and display a life expectancy graph for a given country.

    This function reads life expectancy data from a CSV file,
    filters the row corresponding to the specified country,
    and plots its life expectancy evolution over the years.

    Args:
        country (str): Name of the country to extract data from.

    Raises:
        FileNotFoundError: If the dataset file cannot be found.
        ValueError: If the dataset is empty or the country is not found.
        RuntimeError: If the CSV is malformed or cannot be parsed.
        Exception: For any unexpected errors during processing.

    Notes:
        - The CSV file is expected to have the following format:
          first column as country names and remaining columns as years.
        - The x-axis displays a subset of years (e.g., every ~40 years)
          for better readability.
    """
    try:
        data: pd.DataFrame = load("life_expectancy_years.csv")

        country_data = data[data['country'] == country]
        expectancy = country_data.iloc[0, 1:]
        expectancy_list = expectancy.tolist()
        years = data.columns[1:]
        years_list = years.tolist()

        ticks = ['1800', '1840', '1880', '1920', '1960',
                 '2000', '2040', '2080']

        plt.plot(years_list, expectancy_list)
        plt.xticks(ticks)
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title(f"{country} Life expectancy Projections")
        plt.show()
    except Exception as e:
        raise Exception(f"Problem with the data provided: {e}")


def main():
    try:
        country = 'Kuritiba'
        load_graph(country)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
