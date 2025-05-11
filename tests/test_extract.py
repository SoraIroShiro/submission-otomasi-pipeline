import unittest
from utils.extract import scrape_fashion_studio

class TestExtract(unittest.TestCase):
    def test_scrape_not_empty(self):
        data = scrape_fashion_studio(pages=1)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('Title', data[0])
        self.assertIn('Price', data[0])
        self.assertIn('Rating', data[0])
        self.assertIn('Colors', data[0])
        self.assertIn('Size', data[0])
        self.assertIn('Gender', data[0])
        self.assertIn('timestamp', data[0])

if __name__ == '__main__':
    unittest.main()