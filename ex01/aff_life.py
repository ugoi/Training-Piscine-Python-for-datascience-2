from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Germany Life expectancy Projections"""
    try:
        df = load("life_expectancy_years.csv")
        germany = df[df['country'] == 'Germany']
        life_expectancy_germany = germany.iloc[0, 1:]
        plt.plot(life_expectancy_germany, color='blue')
        plt.title('Germany Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.xticks(life_expectancy_germany.index[::40])
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
