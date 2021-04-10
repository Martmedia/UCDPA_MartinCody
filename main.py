
import pandas as pd
import numpy as np


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def printMostRecentMovie(df):
    #df_sorted = df.sort_values('release_date', ascending=False)
    df.sort_values('release_date', ascending=False, inplace=True)
    print(
        'Original title: ' +
        df['original_title'].iloc[0] +
        ', release date' +
        df['release_date'].iloc[0]
    )


print_hi('PyCharm')

print_hi('Martin')

#file_url = 'https://raw.githubusercontent.com/Martmedia/UCDPA_MartinCody/main/tmdb_movies_data.csv'
file_url = 'tmdb_movies_data.csv'
martmovies = pd.read_csv(file_url)

for x in range(0, 5):
    # print("Genre: " + dataFrame.loc[x, 'genres'] + ", budget: " + str(dataFrame.loc[x, 'budget']))
    print("Genre: " + martmovies.loc[x, 'genres'])
#martmovies.info()
printMostRecentMovie(martmovies)
