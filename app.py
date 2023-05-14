import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests


def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "https://image.tmbd.org/t/p/w500/" + data['poster_path']

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  similar_movies = np.argsort(similarity[movie_index])[::-1][1:6]

  recommended_movies = []
  recommended_movies_posters = []
  for i in similar_movies:
      movie_id = movies.iloc[i].movie_id
      recommended_movies.append(movies.iloc[i].title)
      recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_posters



similarity = pickle.load(open('Similarity_matrix.pkl', 'rb'))

movies_dict = pickle.load(open('Movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('MOVIE RECOMMENDATION')

selected_movie = st.selectbox('What should we recommend you',
                      movies.title.values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])




# movies_list = pickle.load(open('Movies.pkl', 'rb'))
# movies = pd.read_pickle('Movies.pkl')
# movies_list = movies.title.values