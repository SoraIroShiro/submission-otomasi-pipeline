import unittest
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform_output(self):
        sample = [
            {"Title": "T-shirt", "Price": "$10.0", "Rating": "4.5", "Colors": "3", "Size": "M", "Gender": "Men", "timestamp": "2025-05-11T00:00:00"}
        ]
        df = transform_data(sample)
        self.assertEqual(df.shape[0], 1)
        self.assertEqual(df.iloc[0]['Price'], 160000.0)
        self.assertEqual(df.iloc[0]['Rating'], 4.5)

if __name__ == '__main__':
    unittest.main()