from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Germany Life expectancy Projections"""
    try:
        df = load("life_expectancy_years.csv")
        germany = df[df['country'] == 'Germany']
        life_expectancy_germany = germany.iloc[0, 1:].squeeze()
        plt.plot(life_expectancy_germany.index.astype(int),
                 life_expectancy_germany.values,
                 color='blue')
        plt.title('Germany Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
