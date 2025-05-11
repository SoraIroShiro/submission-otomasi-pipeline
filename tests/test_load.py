import unittest
import os
import pandas as pd
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):
    def test_save_to_csv(self):
        df = pd.DataFrame([{"Title": "T-shirt", "Price": 160000.0, "Rating": 4.5, "Colors": "3", "Size": "M", "Gender": "Men", "timestamp": "2025-05-11T00:00:00"}])
        filename = "test_products.csv"
        save_to_csv(df, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()