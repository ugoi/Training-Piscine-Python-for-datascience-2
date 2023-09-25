import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """Load a dataset from the provided path and return it as a DataFrame.
    Args:
    - path (str): Path to the CSV dataset.
    Returns:
    - DataFrame: Loaded dataset.
    Note:
    If there's an error in loading the dataset
    or if the file isn't a .csv file,
    the function will return None.
    """
    if not path.endswith(".csv"):
        print("Error: Not a CSV file.")
        return None
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
