import pandas as pd

def transform_data(data):
    """
    Membersihkan dan mentransformasi data hasil scraping.
    """
    df = pd.DataFrame(data)
    # Hapus baris dengan Price tidak valid
    df = df[df['Price'].str.startswith('$', na=False)]
    # Hapus baris dengan Title 'Unknown Product'
    df = df[df['Title'] != 'Unknown Product']
    # Hapus baris dengan Rating tidak valid
    df = df[~df['Rating'].str.contains('Invalid', na=False)]
    # Hapus duplikat dan null
    df = df.drop_duplicates().dropna()
    # Konversi kolom Price ke float (dalam rupiah)
    df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float) * 16000
    # Konversi kolom Rating ke float
    df['Rating'] = df['Rating'].astype(float)
    # Pastikan kolom lain bertipe string
    df['Colors'] = df['Colors'].astype(str)
    df['Size'] = df['Size'].astype(str)
    df['Gender'] = df['Gender'].astype(str)
    return df