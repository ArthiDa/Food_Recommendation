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
- Takes the necessary columns from the data frame and renames them. Finally, the shape of the data frame is (293,8)
- Export the data frame as a CSV file named 'meals.csv'.

## Preprocessing the dataset

The idea is to make some tags using the 'title', 'instructions', 'category', 'area', and 'tags' columns in the dataset. To do that need to preprocess the dataset. There are some null values in the dataset. I also observed that some values are empty strings. To handle these - 

- I count the total null values for every column. Only one column named 'tags' has all null values. The count of null values for the column is 117. So, instead of dropping the entire rows of null values, I filled them by their 'category' and 'area' values.
- After handling the null values I find that some values in the 'video' column have empty strings. The count of empty strings for the column is 15. So, I dropped them.
- Finally, the dataset has no null values and empty strings.
- To make tags for each meal I just simply added the above mention column.
- At the end of preprocessing, I just apply lowercase in my modified 'tags' column.

## Applying Text Vectorization and Finding Similar Meals using Cosine Distance
From sklearn, I apply CountVectorizer to find the max 1500 words that occur most in the 'tags' column without 'English' stop words. Convert them into NumPy ndarray and calculate the cosine_similarity. Sorted the cosine_similarity in reverse order and only takes the first 5 similar words for particular meals with their index. In the end, we just export the meals modified dataset and similarity array into PKL file.

## Streamlit
Write a Python script to show meals recommendation for selected meals with the help of streamlit app.

## Application Interface
![Recommendation Interface](https://github.com/ArthiDa/Food_Recommendation/blob/main/app_interface.png)

## Reference

This Machine Learning Project was inspired by [CampusX](https://www.youtube.com/@campusx-official)
