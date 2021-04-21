#Import required packages
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import bokeh as bp

#Functions (Reusable Code)
def printMostRecentMovie(df):
    df.sort_values('release_date', ascending=False, inplace=True)
    print("Most recent film in dataset is: " + df['original_title'].iloc[0] + ", released on " + str(df['release_date'].iloc[0].date()) )
    print("Least recent film in dataset is: " + df['original_title'].iloc[-1] + ", released on " + str(df['release_date'].iloc[-1].date()) )
    return

def printMostProfitableMovie(df):
    df.sort_values('profitability', ascending=False, inplace=True)
    print("Most profitable film in dataset is: " + df['original_title'].iloc[0] + ", which had profitability of "
          + str(df['profitability'].iloc[0] )  + ", budget of " +str(df['budget'].iloc[0]) + ", revenue of " + str(df['revenue'].iloc[0]))
    print("Least profitable film in dataset is: " + df['original_title'].iloc[-1] + ", which had profitability of "
          + str(df['profitability'].iloc[-1] ) + ", budget of " + str(df['budget'].iloc[-1]) + ", revenue of " + str(df['revenue'].iloc[-1]))
    return

def removeLowBudgetFilms(df):
    df.drop(df[ df.budget < 500000 ].index, inplace=True)
    return

def removeDocumentaries(df):
    df.drop(df[df.first_genre == "Documentary"].index, inplace=True)
    return

def removeLowRevenueFilms(df):
    df.drop(df[ df.revenue < 50000 ].index, inplace=True)
    return

#Remove all rows 'revenue'/'budget' where value = 0
def removeInvalidRows(df):
    df.drop(df[df.budget == 0].index, inplace=True)
    df.drop(df[df.revenue == 0].index, inplace=True)
    return

def removePreJawsMovies(df):
    df.drop(df[df.release_year < 1975].index, inplace=True)
    return

def addProfitability(df):
    df['profitability'] = df['revenue'] / df['budget']
    return

def addFirstGenre(df):
    df['first_genre'] = df['genres'] .apply( lambda val : val.split('|')[0])
    return

def removeUnnecessaryColumns(df):
    df.drop(['id', 'imdb_id', 'homepage', 'tagline', 'budget_adj', 'revenue_adj', 'vote_count'], inplace=True, axis=1)
    return

def convertReleaseDate(df):
    martmovies['release_date'] = pd.to_datetime(martmovies['release_date'], infer_datetime_format=True, errors='raise')
    return


file_url = 'https://raw.githubusercontent.com/Martmedia/UCDPA_MartinCody/main/tmdb_movies_data.csv'
file_url = 'tmdb_movies_data.csv'
martmovies = pd.read_csv(file_url)

#Cleaning up of dataframe (original = 10866 rows/21cols)

#Convert 'release_date' column to uk-format date object(no datetime dtype indicated)
convertReleaseDate(martmovies)

#Remove uneccessary columns
removeUnnecessaryColumns(martmovies)

#Delete rows wher columns revenue or budget = 0
removeInvalidRows(martmovies)


addProfitability(martmovies)
addFirstGenre(martmovies)

removePreJawsMovies(martmovies)
removeDocumentaries(martmovies)
removeLowBudgetFilms(martmovies)
removeLowRevenueFilms(martmovies)



martmovies.info()


printMostRecentMovie(martmovies)

printMostProfitableMovie(martmovies)

sns.scatterplot(data=martmovies, x="release_date", y="popularity", hue='popularity')



