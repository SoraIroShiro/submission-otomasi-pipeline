import pandas as pd

def save_to_csv(df, filename="products.csv"):
    """
    Menyimpan DataFrame ke file CSV.
    """
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Gagal menyimpan data ke CSV: {e}")

# untuk menyimpan ke Google Sheets
def save_to_gsheet(df, spreadsheet_name, worksheet_name, creds_json="google-sheets-api.json"):
    import gspread
    from gspread_dataframe import set_with_dataframe
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
    client = gspread.authorize(creds)

    try:
        spreadsheet = client.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        spreadsheet = client.create(spreadsheet_name)
        spreadsheet.share('', perm_type='anyone', role='writer')  # Set akses publik editor

    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
        worksheet.clear()
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="1000", cols="20")

    set_with_dataframe(worksheet, df)
    print(f"Data berhasil disimpan ke Google Sheets: {spreadsheet_name} - {worksheet_name}")