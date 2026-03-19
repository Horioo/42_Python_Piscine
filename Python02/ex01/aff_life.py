from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ToDo
# O Eixo do X esta a mostrar os anos toods em vez de apenas os de 20 em 20

def load_graph():
    data: pd.DataFrame = load("life_expectancy_years.csv")
    country = 'France'

    portugal_Data = data[data['country'] == country]
    expectancy = portugal_Data.iloc[0, 1:]
    expectancy_list = expectancy.tolist()
    years = data.columns[1:]
    years_list = years.tolist()

    plt.plot(years_list, expectancy_list)
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title(f"{country} Life expectancy Projections")
    plt.show()


def main():
    load_graph()


if __name__ == "__main__":
    main()
