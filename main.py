#Import required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

def printMostRecentMovie(df):
    df_sorted = df.sort_values('release_date', ascending=False)
    df.sort_values('release_date', ascending=False, inplace=True)
    print(
        'Original title: ' +
        df['original_title'].iloc[0] +
        ', release date' +
        df['release_date'].iloc[0]
    )


file_url = 'https://raw.githubusercontent.com/Martmedia/UCDPA_MartinCody/main/tmdb_movies_data.csv'
file_url = 'tmdb_movies_data.csv'
martmovies = pd.read_csv(file_url)


#for x in range(0, 5):
    # print("Genre: " + dataFrame.loc[x, 'genres'] + ", budget: " + str(dataFrame.loc[x, 'budget']))
    #print("Genre: " + martmovies.loc[x, 'genres'])

printMostRecentMovie(martmovies)

#Cleaning up of dataframe (original = 10866 rows/21cols)

#1. Convert 'release_date' column to uk-format date object(no datetime dtype indicated)
martmovies['release_date'] = pd.to_datetime(martmovies['release_date'])
martmovies.info()

#2. Remove uneccessary columns
martmovies.drop('id', inplace=True, axis=1)
martmovies.drop('imdb_id', inplace=True, axis=1)
martmovies.drop('homepage', inplace=True, axis=1)
martmovies.drop('tagline', inplace=True, axis=1)
martmovies.drop('budget_adj', inplace=True, axis=1)
martmovies.drop('revenue_adj', inplace=True, axis=1)
martmovies.drop('vote_count', inplace=True, axis=1)
print(martmovies.head(3))

martmovies.info()
#3. Remove all rows pre 1975 (see 'Jaws' reference in document)