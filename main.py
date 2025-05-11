
from utils.extract import scrape_fashion_studio
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_gsheet

if __name__ == "__main__":
    data = scrape_fashion_studio()

    # tampilkan 2 data pertama hasil extract
    print(f"Jumlah data hasil extract: {len(data)}")
    print(data[:2])  

    #transform data
    df = transform_data(data)

    # Cek dataframe
    print(df.head())
    print(df.info())

    # Simpan ke CSV
    save_to_csv(df)

    # Simpan ke Google Sheets
    save_to_gsheet(df, "otomasi ETL Pipeline", "Sheet1")
