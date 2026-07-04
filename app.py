import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "2f926434"

def fetch_poster(title):

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"

    data = requests.get(url).json()

    if data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]

    return None

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]])

    return recommended_movies

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    cols = st.columns(5)

    for idx, movie in enumerate(recommendations):

        with cols[idx]:

            poster = fetch_poster(movie['title'])

            if poster:
                st.image(poster)

            st.markdown(f"### 🎬 {movie['title']}")

            st.write(f"⭐ Rating: {movie['vote_average']}")

            year = str(movie['release_date'])[:4]
            st.write(f"📅 Year: {year}")

            overview = " ".join(movie['overview'])[:120] + "..."

            st.write(overview)