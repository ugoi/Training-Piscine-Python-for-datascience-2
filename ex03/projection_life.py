from load_csv import load
from matplotlib import pyplot as plt
from matplotlib.ticker import EngFormatter


def main():
    """Germany Life expectancy Projections"""
    try:
        df_le = load("life_expectancy_years.csv")
        df_le_1900 = df_le['1900']

        df_gdp = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        df_gdp_1900 = df_gdp['1900']

        plt.scatter(df_gdp_1900.values, df_le_1900.values)
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        eng_format = EngFormatter()
        plt.gca().xaxis.set_major_formatter(eng_format)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
