import streamlit as st
import pickle
import pandas as pd
import requests
st.set_page_config(layout="wide")
st.title('Movie recommender System')

def fetch_poster(movie_id):
    response =  requests.get("https://api.themoviedb.org/3/movie/{}?api_key=02f5989cc351dc521260df1d108bf4e5&language=en-US".format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_list)
selected_movie = st.selectbox(
"What movie would you like to watch today?",
(movies['title'].values))

if st.button("Recommend"):
    names , poster = recommend(selected_movie)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.markdown(names[0])
        st.image(poster[0])
    with col2:
        st.markdown(names[1])
        st.image(poster[1])
    with col3:
        st.markdown(names[2])
        st.image(poster[2])
    with col4:
        st.markdown(names[3])
        st.image(poster[3])
    with col5:
        st.markdown(names[4])
        st.image(poster[4])
