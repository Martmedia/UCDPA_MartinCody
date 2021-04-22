#Import required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import bokeh as bp

# Dataset Cleaning as Functions (Reusable Code)
def printMostRecentMovie(df):
    df.sort_values('release_date', ascending=False, inplace=True)
    print("Most recent film in dataset is: " + df['original_title'].iloc[0] + ", released on " + str(df['release_date'].iloc[0].date()) )
    print("Least recent film in dataset is: " + df['original_title'].iloc[-1] + ", released on " + str(df['release_date'].iloc[-1].date()) )
    return

#def printMostProfitableMovie(df):
    #df.sort_values('profitability', ascending=False, inplace=True)
    #print("Most profitable film in dataset is: " + df['original_title'].iloc[0] + ", which had profitability of "
          #+ str(df['profitability'].iloc[0] )  + ", budget of " +str(df['budget'].iloc[0]) + ", revenue of " + str(df['revenue'].iloc[0]))
    #print("Least profitable film in dataset is: " + df['original_title'].iloc[-1] + ", which had profitability of "
          #+ str(df['profitability'].iloc[-1] ) + ", budget of " + str(df['budget'].iloc[-1]) + ", revenue of " + str(df['revenue'].iloc[-1]))
    #return

#Remove all rows 'revenue'/'budget' where value = 0 as this has a serious distorting effect on output
def removeInvalidRows(df):
    df.drop(df[df.budget == 0].index, inplace=True)
    df.drop(df[df.revenue == 0].index, inplace=True)
    return

#There are movies which are clearly outliers based on budget to revenue ratio.They need to be dropped
def removeLowRevenueFilms(df):
    df.drop(df[ df.revenue < 50000 ].index, inplace=True)
    return

def removeLowBudgetFilms(df):
    df.drop(df[ df.budget < 500000 ].index, inplace=True)
    return

#Documentaries are relatively rare gene type and are not generally bundled with commercial output
def removeDocumentaries(df):
    df.drop(df[df.first_genre == "Documentary"].index, inplace=True)
    return

#Drop all movies pre 1975 to measure the 'Jaws effect'
def removePreJawsMovies(df):
    df.drop(df[df.release_year < 1975].index, inplace=True)
    return

#def addProfitability(df):
    #df['profitability'] = df['revenue'] / df['budget']
    #return

#Add new column 'first_genre' streamlining original 'genre' column, then print to ensure change is good
def addFirstGenre(df):
    df['first_genre'] = df['genres'].apply(lambda val: val.split('|')[0])
    df['first_genre'].value_counts()
    print(martmovies['first_genre'].value_counts())
    return

#Drop columns that have no useful function in this analysis
def removeUnnecessaryColumns(df):
    df.drop(['imdb_id', 'homepage', 'tagline', 'budget_adj', 'revenue_adj', 'vote_count'], inplace=True, axis=1)
    return

def convertReleaseDate(df):
    martmovies['release_date'] = pd.to_datetime(martmovies['release_date'], infer_datetime_format=True, errors='raise')
    return


# Pull dataset into Pandas dataframe
file_url = 'https://raw.githubusercontent.com/Martmedia/UCDPA_MartinCody/main/tmdb_movies_data.csv'
file_url = 'tmdb_movies_data.csv'
martmovies = pd.read_csv(file_url)


#Calling of functions:

#Convert 'release_date' column to uk-format date object(no datetime dtype indicated)
convertReleaseDate(martmovies)
martmovies['release_date'].head()

#Remove uneccessary columns
removeUnnecessaryColumns(martmovies)

#Delete rows where columns revenue or budget = 0
removeInvalidRows(martmovies)


addFirstGenre(martmovies)

removePreJawsMovies(martmovies)
removeDocumentaries(martmovies)
removeLowBudgetFilms(martmovies)
removeLowRevenueFilms(martmovies)


martmovies.info()


printMostRecentMovie(martmovies)

#printMostProfitableMovie(martmovies)

print(martmovies["revenue"].max())

#1. LINE PLOT OF TOTAL RELEASE NUMBERS BY YEAR
# Create group for each year and then count movie release totals per year
data=martmovies.groupby('release_year').count()['id']
print(data.tail())
martmovies.groupby('release_year').count()['id'].plot(xticks = np.arange(1975,2016,5))

sns.set(rc={'figure.figsize':(12,7)})
plt.title("Total Movies Released by Year",fontsize = 14)
plt.xlabel('Release year',fontsize = 10)
plt.ylabel('Number Of Movies',fontsize = 10)

sns.set_style("whitegrid")
plt.show()

#2. HIGHEST EARNING MOVIES 1975-2015



