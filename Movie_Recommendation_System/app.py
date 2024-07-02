import streamlit as st
import pandas as pd
import pickle

# Load the movies and similarity matrix
movies_path = 'movies.pkl'
similarity_path = 'similarity.pkl'

with open(movies_path, 'rb') as f:
    movies = pickle.load(f)
    
with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)
st.markdown("""
    <style>
    .title {
        color: red;
        font-size: 50px;
        font-weight: bold;
        text-align:center;
    }
    .write {
        color: red;
        font-size: 18px;
        font-weight: bold; 
        text-align:center;       
    
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
st.markdown('<p class="title">Recommender System</p><p class="write">---By Ritika Saini---</p>', unsafe_allow_html=True)
movie_selected = st.selectbox('Select a movie you like:', movies['title'].values)

def recommend_movie(movie):
    if movie not in movies['title'].values:
        st.error("Movie not found in database.")
        return []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button('Recommend'):
    if movie_selected:
        recommendations = recommend_movie(movie_selected)
        if recommendations:
            st.write('Movies recommended for you:')
            for movie in recommendations:
                st.write(movie)
    else:
        st.error("Please enter a movie name.")
