
import unittest
from load_csv import load
import pandas as pd


class TestLoadCSV(unittest.TestCase):
    def test_valid_path(self):
        df = load("life_expectancy_years.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(df.shape, (0, 0))

    def test_invalid_path(self):
        df = load("non_existent_file.csv")
        self.assertIsNone(df)

    def test_invalid_format(self):
        df = load("some_non_csv_file.txt")
        self.assertIsNone(df)

if __name__ == "__main__":
    unittest.main()
