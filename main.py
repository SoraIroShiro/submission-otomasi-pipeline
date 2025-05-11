
##fungsi transform
from utils.extract import scrape_fashion_studio
from utils.transform import transform_data

if __name__ == "__main__":
    data = scrape_fashion_studio()
    print(f"Jumlah data hasil extract: {len(data)}")
    print(data[:2])  # tampilkan 2 data pertama hasil extract
    df = transform_data(data)
    print(df.head())



## Fungsi Load
from utils.extract import scrape_fashion_studio
from utils.transform import transform_data
from utils.load import save_to_csv

if __name__ == "__main__":
    data = scrape_fashion_studio(pages=2)
    print(f"Jumlah data hasil extract: {len(data)}")
    print(data[:2])  # tampilkan 2 data pertama hasil extract
    df = transform_data(data)
    print(df.head())
    save_to_csv(df)