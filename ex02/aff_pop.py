import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from load_csv import load


def eng_to_f(series):
    """
    Convert a series with population values in
    'M' and 'k' notations to actual numbers.
    """
    return series.str.replace('M', 'e6').str.replace('k', 'e3').astype(float)


def plot_population_comparison(df):
    """Plot population comparison of Germany and Switzerland."""
    germany_data = eng_to_f(
        df[df['country'] == 'Germany'].iloc[:, 1:252].squeeze())
    switzerland_data = eng_to_f(
        df[df['country'] == 'Switzerland'].iloc[:, 1:252].squeeze())

    plt.plot(
        germany_data.index.astype(int),
        germany_data.values,
        label='Germany',
        color='blue')
    plt.plot(
        switzerland_data.index.astype(int),
        switzerland_data.values,
        label='Switzerland',
        color='red')

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')
    eng_format = EngFormatter()
    plt.gca().yaxis.set_major_formatter(eng_format)
    plt.tight_layout()
    plt.show()


def main():
    """main"""
    dataset_path = "population_total.csv"
    df = load(dataset_path)
    plot_population_comparison(df)


if __name__ == "__main__":
    main()
