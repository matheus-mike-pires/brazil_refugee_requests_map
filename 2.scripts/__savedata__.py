from __statistics__ import *
from __main__ import *
import pandas as pd


def load_raw_data():
    open_data1 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_1994_2023.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data2 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2024.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data3 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2025.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data4 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_01.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data5 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_02.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data6 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_03.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data7 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_04.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data8 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_05.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data9 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_06.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    open_data10 = pd.read_csv('SOLICITANTES_REFUGIO_DIV_2026_07.csv', on_bad_lines='skip', encoding_errors='ignore',sep=';', encoding='latin1', low_memory=False)
    
    update_data = pd.concat([open_data1, open_data2, open_data3, open_data4, open_data5, open_data6, open_data7, open_data8, open_data9, open_data10])
    
    return update_data
    


def save_csv(dataframes):
    name_of_file = input('Write the file name: ')
    dataframes.to_csv(f'{name_of_file}.csv', index=False)
    print()
    print('DataFrame has been saved!')
    print()
    
def save_txt(elementdf):
    name_of_file = input('input file name: ')
    with open(f'{name_of_file}.txt', 'w') as file:
        file.write(f'- Between 1994 and 2016 (before legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[0]}% of the total refugees. During legislation change (2017 - 2018), they represented {avg_results[1]}% of the total refugees. Between 2019 and 2026 (after legislation change), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[2]}% of the total refugees. Considering 2017 to 2026 they represented {avg_results[3]}% of the total refugees. In the intire dataset (from 1994 to 2026), refugees from {nationality_chosen_in_filter[0]} represented {avg_results[4]}% of the total refugees. This data was obtained with the open source tool migration_flow.py, avaliable at the repository [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]. The raw data was obtained via CONAIRE (source [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]. Feel free to use it in your researches or work! If you need help, contact me [matheusolv.pires@gmail.com')