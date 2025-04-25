import streamlit as st
import pickle
import pandas as pd
import difflib
import requests

# TMDb API key
API_KEY = "Replace With Your TMDB Api Key"

# Load movie data and similarity matrix
movies = pd.read_pickle("movies.pkl")
similarity = pickle.load(open("similarity.pkl", "rb"))

# Function to fetch poster from TMDb
def fetch_poster(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": API_KEY,
            "query": title
        }
        response = requests.get(url, params=params, timeout=10)  # ✅ added timeout
        response.raise_for_status()  # ✅ will raise HTTPError if status is 4xx or 5xx

        data = response.json()

        if data["results"]:
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except requests.exceptions.Timeout:
        st.error(f"⚠️ Timeout while fetching poster for '{title}'")
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Error fetching poster for '{title}': {e}")
    return None  # return None if fetch fails

# Recommendation logic
def recommend(movie_name):
    movie_list = movies["title"].tolist()
    close_match = difflib.get_close_matches(movie_name, movie_list, n=1, cutoff=0.6)

    if not close_match:
        return [], []

    index = movies[movies.title == close_match[0]].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    recommended_posters = []

    for i in sorted_movies[1:6]:  # Top 5 recommendations
        title = movies.iloc[i[0]]["title"]
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters

# Streamlit UI setup
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Simple Movie Recommender")

movie_input = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    with st.spinner("Finding similar movies..."):
        movie_names, posters = recommend(movie_input)

        if movie_names:
            st.success("Recommended Movies:")
            cols = st.columns(5)
            for i in range(len(movie_names)):
                with cols[i]:
                    if posters[i]:
                        st.image(posters[i], use_container_width=True)
                    else:
                        st.write("📷 Poster not available")
                    st.caption(movie_names[i])
        else:
            st.warning("❌ No similar movies found. Try a different title.")
