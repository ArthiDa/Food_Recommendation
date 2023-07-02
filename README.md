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

- Fetch all meals by first letter from mealdb API ( www.themealdb.com/api/json/v1/1/search.php?f={a-z} ).
- Convert JSON to pandas data frame.
- Takes the necessary series from the data frame and renames. Finally, shape of the data frame is (293,8)
- Finally export the data frame as a CSV file named 'meals.csv'.

## Preprocessing the dataset

There are some null values in the dataset. I also observed that some values are empty strings. To handle these - 

- I count the total null values for every column. Only one column named 'tags' has all null values. The count of null values for the column is 117. So, instead of dropping the entire rows of null values, I filled them by their 'category' and 'area' values.
- After handling the null values I find that some values in the 'video' column have empty strings. The count of empty strings for the column is 15. So, I dropped them.
- Finally, the dataset has no null values and empty strings.


