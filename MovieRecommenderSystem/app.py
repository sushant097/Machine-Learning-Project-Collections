import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bf942dfb3a2c85876be40228f5cd76e6&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    # Find the index of the given movie
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for movie in movies_list:
        movie_id = movies.iloc[movie[0]].id
        recommended_movies.append(movies.iloc[movie[0]].title)
        # fetch poster from TMDB API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


def load_files():
    movies_dict_load = pickle.load(open('movies_dict.pkl', 'rb'))
    movies_df = pd.DataFrame(movies_dict_load)
    similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
    return movies_dict_load, movies_df, similarity_matrix


movies_dict, movies, similarity = load_files()

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Enter movie title', movies['title'].values)

if st.button("Recommend"):
    movies_name, movies_poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movies_name[0])
        st.image(movies_poster[0])
    with col2:
        st.text(movies_name[1])
        st.image(movies_poster[1])
    with col3:
        st.text(movies_name[2])
        st.image(movies_poster[2])
    with col4:
        st.text(movies_name[3])
        st.image(movies_poster[3])
    with col5:
        st.text(movies_name[4])
        st.image(movies_poster[4])

