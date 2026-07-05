import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import boto3

load_dotenv()  # Load environment variables from .env file

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")

st.markdown("""
Discover movies similar to your favorites.

Select a movie below and we'll recommend 5 similar movies based on content.
""")
st.divider()

# similarity = pickle.load(open("similarity.pkl", "rb"))
# movies = pickle.load(open("movies.pkl", "rb"))

# Load pickle files
# with open("similarity.pkl", "rb") as f:
#   similarity = pickle.load(f)

# with open("movies.pkl", "rb") as f:
#     movies = pickle.load(f)

@st.cache_resource
def load_file(key):
    s3 = get_s3_client()
    bucket = os.getenv("S3_BUCKET_NAME")

    obj = s3.get_object(Bucket=bucket, Key=key)
    return pickle.loads(obj["Body"].read())


movies = load_file("movies.pkl")
similarity = load_file("similarity.pkl")

movies = pd.DataFrame(movies)

movie_list = movies['title'].values

selected_movie_name = st.selectbox(
    "Select a movie:",
    movie_list
)


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, os.getenv("TMDB_API_KEY")))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from TMDB API
        recommended_posters.append(fetch_poster(movie_id))
        
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_posters

if st.button("Recommend", use_container_width=True):
    with st.spinner("Finding recommendations..."):
        names, posters = recommend(selected_movie_name)

    st.success("Here are some movies you might enjoy!")


    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.subheader(names[i])
            st.image(posters[i])


