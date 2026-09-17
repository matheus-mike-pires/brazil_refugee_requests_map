from __savedata__ import *
from __statistics__ import *
import matplotlib.pyplot as plt

def plot_global_overview(global_dfs, all_groups):
    pizza_sizes = [len(all_groups[0]), len(all_groups[1]), len(all_groups[2])]
    pizza_labels = ['Before Law\n(1994-2016)', 'Implementation\n(2017-2018)', 'After Law\n(2019-2026)']
    
    
    years_extracted = global_dfs['DATA_ENTRADA'].str[-4:]
    year_counts = years_extracted.value_counts()
    
    list_y = list(range(1994, 2027))
    list_x = [year_counts.get(str(year), 0) for year in list_y] 

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].plot(list_y, list_x, color='darkblue', marker='o', linewidth=2)
    axs[0].set_title('Total Requests per Year', fontsize=12)
    axs[0].tick_params(axis='x', rotation=45)
    axs[0].grid(True, linestyle='--', alpha=0.6)

    axs[1].pie(pizza_sizes, labels=pizza_labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
    axs[1].set_title('Share by Legislation Period', fontsize=12)

    axs[2].scatter(list_y, list_x, color='darkred', s=60, alpha=0.8, edgecolor='black')
    axs[2].set_title('Distribution Spread', fontsize=12)
    axs[2].tick_params(axis='x', rotation=45)
    axs[2].grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()


def plot_filtered_overview(filtered_df, groups_made, nationality_name):
    
    pizza_sizes = [len(groups_made[3]), len(groups_made[4]), len(groups_made[5])]
    pizza_labels = ['Before Law\n(1994-2016)', 'Implementation\n(2017-2018)', 'After Law\n(2019-2026)']
    
   
    years_extracted = filtered_df['DATA_ENTRADA'].str[-4:]
    year_counts = years_extracted.value_counts()
    
    list_y = list(range(1994, 2027)) 
    list_x = [year_counts.get(str(year), 0) for year in list_y] 

   
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f'Refugee Flow Analysis: {nationality_name}', fontsize=14, fontweight='bold')

     
    axs[0].plot(list_y, list_x, color='darkgreen', marker='o', linewidth=2)
    axs[0].set_title('Requests per Year', fontsize=12)
    axs[0].tick_params(axis='x', rotation=45)
    axs[0].grid(True, linestyle='--', alpha=0.6)

    
    if sum(pizza_sizes) > 0:
        axs[1].pie(pizza_sizes, labels=pizza_labels, autopct='%1.1f%%', startangle=140, colors=['#ffb3e6','#c2c2f0','#ffcc99'])
    axs[1].set_title('Share by Legislation Period', fontsize=12)

 
    axs[2].scatter(list_y, list_x, color='purple', s=60, alpha=0.8, edgecolor='black')
    axs[2].set_title('Distribution Spread', fontsize=12)
    axs[2].tick_params(axis='x', rotation=45)
    axs[2].grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()
    

