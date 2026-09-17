from __statistics__ import *
from __main__ import *
import pandas as pd

open_data1 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_1994_2023.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data2 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2024.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data3 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2025.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data4 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_01.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data5 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_02.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data6 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_03.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data7 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_04.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data8 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_05.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data9 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_06.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
open_data10 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_07.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='utf-8', low_memory=False)
    
update_data = pd.concat([open_data1, open_data2, open_data3, open_data4, open_data5, open_data6, open_data7, open_data8, open_data9, open_data10])

df1 = update_data.drop(['PAIS_DE_NASCIMENTO', 'EST_CIV', 'MUN_RECEBIMENTO'], axis=1)
dataframe = df1
    
def save_csv(dataframes):
    name_of_file = input('Write the file name: ')
    dataframes.to_csv(f'{name_of_file}.csv', index=False)
    print()
    print('DataFrame has been saved!')
    print()
    
def display_any_dataframe(dataframes):
    print(dataframes)
    possible_opt = ['1', '2', '3']
    print('\n This is the currenct version of the DataFrame (updated until 07/30/2026) \n')
    print('1. Display full dataframe (not recommended)')
    print('2. Save it as CSV')
    print('3. Return \n')
    choice = input('Select an option: ')
    while choice not in possible_opt:
        choice = input('Please, select a valid option: ')
    if choice == '1':
        print('\n Loading the DataFrame: \n')
        print(dataframes.to_string())
        display_any_dataframe(dataframes)
    if choice == '2':
        save_csv(dataframes)
    if choice == '3':
        pass
