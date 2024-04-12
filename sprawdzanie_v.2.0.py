import pandas as pd

# Odczytujemy pliki Excel.
dane_df = pd.read_excel('dane.xlsx')
wykaz_df = pd.read_excel('wykaz.xlsx')

# Zakładamy, że pliki mają kolumny 'Bezeichnung', 'Zeinr', 'TYP', 'TECHNOLOGIA', ale należy to zweryfikować.
# W tym przypadku przyjmujemy, że kolumny w pliku 'dane.xlsx' mają '...' na końcu, jak w Twoim przykładzie.

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
