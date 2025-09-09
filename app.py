import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    
    try:
        response = requests.get(
            f'api',
            timeout=10  # Add timeout to avoid long hangs
        )
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.HTTPError as poster_error:
        print("HTTP Error:", poster_error)
    except requests.exceptions.ConnectionError as poster_error_1:
        print("Connection Error:", poster_error_1)
    except requests.exceptions.Timeout as poster_error_2:
        print("Timeout Error:", poster_error_2)
    except requests.exceptions.RequestException as poster_error_3:
        print("Request Error:", poster_error_3)
    return "https://via.placeholder.com/500x750?text=Image+Not+Found"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movie_posters
    
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    # First row
    cols1 = st.columns(5)
    for i in range(5):
        with cols1[i]:
            st.text(names[i])
            st.image(posters[i])

    # Second row
    cols2 = st.columns(5)
    for i in range(5, 10):
        with cols2[i - 5]:
            st.text(names[i])
            st.image(posters[i])