import pandas as pd

# Odczytujemy plik Excel.
wynik_df = pd.read_excel('wynik.xlsx')

# Przechodzimy przez DataFrame i sprawdzamy kolumny 'Stufe' oraz 'Technologia'.
for index, row in wynik_df.iterrows():
    current_stufe = row['Stufe']
    if row['TECHNOLOGIA'] in ['GS', 'S', 'SO']:
        # Szukamy najbliższego wyższego elementu 'Stufe - 1' w górę od bieżącej pozycji.
        # Iterujemy wstecz od bieżącej pozycji.
        for previous_index in range(index - 1, -1, -1):
            if wynik_df.at[previous_index, 'Stufe'] < current_stufe:
                # Jeśli znaleźliśmy nadrzędny element i kolumna 'technologia_ze_starego' jest pusta,
                # wpisujemy 'C'.
                if pd.isna(wynik_df.at[previous_index, 'technologia_ze_starego']):
                    wynik_df.at[previous_index, 'technologia_ze_starego'] = 'C'
                break  # Przerywamy pętlę po znalezieniu pierwszego nadrzędnego elementu.

# Zapisujemy zmodyfikowany DataFrame do nowego pliku Excel.
wynik_df.to_excel('wynik_updated.xlsx', index=False)
