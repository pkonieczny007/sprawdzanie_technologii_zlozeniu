import pandas as pd

# Odczytujemy pliki Excel.
try:
    dane_df = pd.read_excel('dane.xlsx')
    wykaz_df = pd.read_excel('wykaz.xlsx')
except FileNotFoundError as e:
    print(f"STATUS. Błąd. Nie znaleziono pliku: {e}")
    exit()

# Wymagane kolumny dla plików
required_columns_dane = ['Bezeichnung', 'Zeinr', 'TECHNOLOGIA']
required_columns_wykaz = ['Bezeichnung', 'Zeinr', 'TYP']

# Sprawdzenie, czy wymagane kolumny istnieją w danych DataFrame
missing_columns_dane = [col for col in required_columns_dane if col not in dane_df.columns]
missing_columns_wykaz = [col for col in required_columns_wykaz if col not in wykaz_df.columns]

if missing_columns_dane or missing_columns_wykaz:
    print("STATUS. Błąd. Sugestia poprawy:")
    for col in missing_columns_dane:
        print(f"{col} - BRAK kolumny w 'dane.xlsx'")
    for col in missing_columns_wykaz:
        print(f"{col} - BRAK kolumny w 'wykaz.xlsx'")
else:
    print("STATUS. Wykaz kompletny.")
    print("Trwa przetwarzanie.")

    # Dodajemy nową kolumnę do DataFrame 'wykaz'.
    wykaz_df['technologia_ze_starego'] = pd.NA

    # Przetwarzamy DataFrame 'wykaz'.
    for index, row in wykaz_df.iterrows():
        if row['TYP'] == 'ZŁOŻENIE':
            # Szukamy pasujących wierszy w DataFrame 'dane'.
            match = dane_df[(dane_df['Bezeichnung'] == row['Bezeichnung']) & (dane_df['Zeinr'] == row['Zeinr'])]
            if not match.empty:
                # Jeśli znajdziemy pasujący wiersz, aktualizujemy kolumnę 'technologia_ze_starego'.
                wykaz_df.at[index, 'technologia_ze_starego'] = match.iloc[0]['TECHNOLOGIA']

    # Zapisujemy zmodyfikowany DataFrame 'wykaz' do nowego pliku Excel.
    wykaz_df.to_excel('wynik.xlsx', index=False)
    print("Gotowe.")
