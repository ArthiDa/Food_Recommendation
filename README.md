# Food Recommender System

In this Machine Learning Project, I tried to create a recommender system that recommends the top 5 similar food for a particular selected food.

## Important Python Libraries Used In The Project

- Pandas
- NumPy
- Requests
- Sklearn
- Nltk
- Streamlit

## Create Dataset Using mealdb API

- Fetch all meals by first letter from mealdb [api](www.themealdb.com/api/json/v1/1/search.php?f=a).
- Convert json to pandas dataframe.
- Takes the importants series from the dataframe.
- Finally export the dataframe as a csv file named 'meals.csv'.

