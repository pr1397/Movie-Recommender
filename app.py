import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=1bd837f37ec1bd0dbdc7f70b8be8ca7b&language=en-US.format(movie_id)')
#     data = response.json()
#     st.write(data)
#     full_path = "https://image.tmdb.org/t/p/w185/" + data['poster_path']
#     return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    recommended_movies = []
    # recommended_movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies

mv = open('c:/Users/prashasti/Movie Recommender/movies_dict.pkl','rb')
movies_dict = pickle.load(mv)
movies= pd.DataFrame(movies_dict)
similarity = pickle.load(open('c:/Users/prashasti/Movie Recommender/similarity.pkl','rb'))
st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)