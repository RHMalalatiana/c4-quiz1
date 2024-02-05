# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:22:10 2024

@author: Malala
"""
"""
EXTRACT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("movie_dataset.csv")

"""
TRANSFORM
"""
#view the column name
column_name=list(df.columns)
print(column_name)

"""
['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
"""
#remove the space in the column name
df.rename(columns = {"Runtime (Minutes)":"Runtime(minutes)"}, inplace = True)
df.rename(columns = {"Revenue (Millions)":"Revenue(Millions)"}, inplace = True)

#Question 1
highest_rated_movie=df[df["Rating"]==df["Rating"].max()]
print("Question 1 \n The highest rated movie in the dataset is ", highest_rated_movie["Title"])

#Question 2
average_revenue= df["Revenue(Millions)"].mean()
df["Revenue(Millions)"].fillna(average_revenue, inplace = True) 
print("Question 2 \n The average revenue of all movies is", df["Revenue(Millions)"].mean())

#Question 3
df_2015_2017=df[(df["Year"]>=2015)& (df["Year"]<=2017)]
print("Question 3 \n The average revenue of all movies from 2015 to 2017 is", df_2015_2017["Revenue(Millions)"].mean())

#Question 4
df_2016=df[df["Year"]==2016]
print("Question 4 \n The number of movies released in 2016 is ",len(df_2016))

#Question 5
df_Christopher=df[df["Director"]=="Christopher Nolan"]
print("Question 5 \n The number of movies directed by Christopher Nolan is ",len(df_Christopher))

#Question 6
print("Question 6 \n The number of movies in the dataset with a rating of at least 8.0 is ", len(df[df["Rating"]>=8.0]))

#Question 7
print("Question 7 \n The median rating of movies directed by Christopher Nolan is", df_Christopher["Rating"].median())

#Question 8
average_ratings_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_ratings_by_year.idxmax()
print("Question 8 \n The year with the highest average rating is", year_highest_average_rating)

#Question 9
increase=len(df[df["Year"]==2016]) - len(df[df["Year"]==2006])
percentage=(increase/len(df[df["Year"]==2006]))*100
print("Question 9 \n The percentage increase in number of movies made between 2006 and 2016 is",percentage)

#Question 10
actors_list = df["Actors"].str.split(",").explode().str.strip()
actor_counts = actors_list.value_counts()
most_common_actor = actor_counts.idxmax()
print("Question 10 \n The most common actor is:", most_common_actor)

#Question 11
genre_list=df["Genre"].str.split(",").explode().str.strip()
genre_counts = genre_list.value_counts()
print("Question 11 \n The number of genre in the dataset are ", len(genre_counts))

#Question 12
# Calculate the correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix')
plt.show()

