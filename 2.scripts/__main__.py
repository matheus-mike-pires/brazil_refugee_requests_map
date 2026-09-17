from  __statistics__ import *
from __savedata__ import *
import pandas as pd

running_program = []

print('***********************')
print('This is a python program made to explore the data on refugees  in Brasil')
print('The analisys mainly relies on the python library Pandas and on the statistical analysis of the data gathered. ')
print('for more information, acess the repository: ')
print('!!! Follow the instructions on READ.ME to download the necessary files and properly run this program !!!\n')
print('***********************')

def main(dataframe, running_program):
    valid_options = ['1', '2', '3', '4', '5', '6']
    print('\n1. Verify the full database of refuge requests')
    print('2. Graphics')
    print('3. Verify the statistcs')
    print('4. Request contact')
    print('5. How to use')
    print('6. Exit \n')
    choice = input('select an option: ')
    while choice not in valid_options:
        choice = input('please, select a valid option: ')
    if choice == '1':
        display_any_dataframe(dataframe)
    if choice == '2':
        print('not yet done \n')
    if choice == '3':
        statistical_analysis(dataframe)
    if choice == '4':
        print('if you need help or have any suggestions, feel free to contact me:')
        print('matheusolv.pires@gmail.com \n')
    if choice == '5':
        print('Acess the following repository: XXXXXXXXXXXXXXXXXX')
        print('click on the README.md file')
        print('Follow the instructions displayed \n')       
    if choice == '6':
        running_program.append(1)
        print('Thank you for using this program \n')
        running_program = False
    
    

if __name__ == '__main__':
    while len(running_program) == 0:
        main(dataframe, running_program)
