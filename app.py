import streamlit as st
import pickle
import pandas as pd
import requests

# Page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTitle {
        color: #E50914;
        font-size: 3rem !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to fetch movie poster from TMDb API
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e358a9a14599eb585ea6af28fb70edc9"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except:
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

# Recommendation function
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))

        return recommended_movies, recommended_movies_posters
    except IndexError:
        st.error("Movie not found in database!")
        return [], []

# Load the saved model
try:
    movies_dict = pickle.load(open('movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found! Please run the Jupyter notebook first to generate the model.")
    st.stop()

# App title
st.title('🎬 Movie Recommender System')
st.markdown("---")

# Movie selection
st.subheader("Select a movie to get recommendations")
selected_movie = st.selectbox(
    "Choose a movie:",
    movies['title'].values,
    index=None,
    placeholder="Start typing to search..."
)

# Recommendation button
if st.button('Get Recommendations'):
    if selected_movie:
        with st.spinner('Finding similar movies...'):
            names, posters = recommend(selected_movie)

        if names:
            st.markdown("---")
            st.subheader(f"Movies similar to '{selected_movie}':")

            # Display recommendations in columns
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    st.image(posters[idx], use_column_width=True)
                    st.markdown(f"**{names[idx]}**")
    else:
        st.warning("Please select a movie first!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built with Streamlit | Data from TMDb"
    "</div>",
    unsafe_allow_html=True
)
