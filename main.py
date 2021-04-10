
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#
print_hi('PyCharm')

print_hi('Martin')

file_url = 'https://raw.githubusercontent.com/Martmedia/UCDPA_MartinCody/main/tmdb_movies_data.csv'
martmovies = pd.read_csv(file_url)

for x in range(0, 5):
    # print("Genre: " + dataFrame.loc[x, 'genres'] + ", budget: " + str(dataFrame.loc[x, 'budget']))
    print("Genre: " + martmovies.loc[x, 'genres'])
martmovies.info()


