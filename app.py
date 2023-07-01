import streamlit as st
import pickle
import pandas as pd
import requests

meals_dict = pickle.load(open('meals_dict.pkl','rb'))
meals = pd.DataFrame(meals_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(meal):
    meal_index = meals[meals['title'] == meal].index[0]
    distances = similarity[meal_index]
    meals_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_meals = []
    recommended_meals_images = []
    for i in meals_list:
        recommended_meals.append(meals.iloc[i[0]].title)
        recommended_meals_images.append(meals.iloc[i[0]].image)
    return recommended_meals, recommended_meals_images


st.title('Food Recommendation')
selected_meal_name = st.selectbox(
    'Type and Select Food',
    meals['title'].values)

if st.button('Recommend'):
    names, images = recommend(selected_meal_name)
    col = st.columns(5)
    for i in range(5):
        with col[i]:
            st.text(names[i])
            st.image(images[i])