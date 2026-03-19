from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

# ToDo
# O Eixo do X esta a mostrar os anos toods em vez de apenas os de 20 em 20


def load_graph(country: str):
    """
    Function to Load a graph with the Country provided

    Args:
        country (str): Country to get the data from
    """
    try:
        data: pd.DataFrame = load("life_expectancy_years.csv")

        portugal_Data = data[data['country'] == country]
        expectancy = portugal_Data.iloc[0, 1:]
        expectancy_list = expectancy.tolist()
        years = data.columns[1:]
        years_list = years.tolist()

        ticks = ['1800', '1840', '1880', '1920', '1960',
                 '2000', '2040', '2080']

        labels = [str(tick) for tick in ticks]

        plt.plot(years_list, expectancy_list)
        plt.xticks(ticks, labels=labels)
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title(f"{country} Life expectancy Projections")
        plt.show()
    except Exception as e:
        raise Exception(f"Problem with the data provided {e}") from None


def main():
    country = 'Portugal'
    load_graph(country)


if __name__ == "__main__":
    main()
